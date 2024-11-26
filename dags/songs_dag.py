import os
import spotipy
from airflow.models import Variable
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
from youtube_class import YoutubeClient
from spotify_class import SpotifyClient
import psycopg2
import pandas as pd
from io import StringIO
import csv
import logging

logging.basicConfig(
    level=logging.INFO,  # 로그 레벨을 INFO로 설정
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def extract_data_from_site(song_title):
    """ Spotify에서 추천곡을 가져오는 함수 """
    youtube_client = YoutubeClient()
    search_video_df, search_playlist_df = youtube_client.search_youtube(song_title + " music")
    logger.info(f"youtube 추천곡 _ 데이터를 성공적으로 가져왔습니다: {search_video_df}, {search_playlist_df}")
    
    """ Spotify에서 추천곡을 가져오는 함수 """
    spotify_client = SpotifyClient()
    recommendations_data = spotify_client.get_recommendations(song_title)
    logger.info(f"spotify 추천곡 _ 데이터를 성공적으로 가져왔습니다: {recommendations_data}")

    return search_video_df, recommendations_data

def bulk_insert_table(cursor, conn, df, table_name):
    """
    데이터프레임을 PostgreSQL 테이블에 COPY 명령으로 빠르게 삽입.
    """
    # 데이터프레임을 CSV 형식으로 메모리에 저장
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False, quotechar='"', quoting=csv.QUOTE_ALL)
    buffer.seek(0)

    try:
        # COPY 명령 실행
        cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", buffer)
        logger.info(f"youtube 검색 _ 테이블 {table_name}에 데이터 삽입 완료")
    except Exception as e:
        # 에러 발생 시 트랜잭션 롤백
        conn.rollback()
        logger.error(f"youtube 검색 _ {table_name} 삽입 오류: {e}")
    finally:
        buffer.close()

def transform_schema(cursor):
    # search_songs
    # 1. 테이블 삭제
    logger.info(f" search songs : 데이터를 삭제합니다.")
    drop_table_query = "DROP TABLE IF EXISTS django_schema.search_songs;"
    cursor.execute(drop_table_query)
    
    # 2. 테이블 생성
    create_table_query = """
    CREATE TABLE django_schema.search_songs (
        no SERIAL PRIMARY KEY,
        song_title VARCHAR(255) NOT NULL,
        song_url VARCHAR(255) NOT NULL,
        thumbnail VARCHAR(255),
        platform VARCHAR(255) NOT NULL
    );
    """
    cursor.execute(create_table_query)
    logger.info(" search_songs _ 새 테이블 생성 완료")

    
    # 3. search_youtube_video 데이터를 search_songs에 삽입
    youtube_query = """
    INSERT INTO django_schema.search_songs (song_title, song_url, thumbnail, platform)
    SELECT 
        video_title AS song_title,
        video_id AS song_url,
        CONCAT('https://img.youtube.com/vi/', video_id, '/0.jpg') AS thumbnail,
        'youtube' AS platform
    FROM playlist_schema.search_youtube_video;
    """
    cursor.execute(youtube_query)

    # 4. spotify_recommend 데이터를 search_songs에 삽입
    spotify_query = """
    INSERT INTO django_schema.search_songs (song_title, song_url, thumbnail, platform)
    SELECT 
        title AS song_title,
        link AS song_url,
        cover_image AS thumbnail,
        'spotify' AS platform
    FROM playlist_schema.spotify_recommend;
    """
    cursor.execute(spotify_query)
    logger.info(f" search songs : 데이터가 삽입 되었습니다.")

    return


def load_data_to_db(search_video_df, recommendations_data):
    """ 데이터베이스에 데이터 로드 """
    if search_video_df.empty:
        logger.warning("youtube 검색 _ 테이블에 빈 테이블이 있습니다.")
        return
    if not recommendations_data:
        logger.warning("spotify 추천곡 _ 로드할 데이터가 없습니다.")
        return

    pg_hook = PostgresHook(postgres_conn_id='playlist')  # 연결 ID 사용
    conn_tmp = pg_hook.get_connection(pg_hook.postgres_conn_id)
    # 직접 psycopg2로 연결하고 인코딩을 설정
    try:
        conn = psycopg2.connect(
            host=conn_tmp.host,
            database=conn_tmp.schema,
            user=conn_tmp.login,
            password=conn_tmp.password,
            port=conn_tmp.port,
            client_encoding='UTF8'  # 인코딩 설정
        )
        cursor = conn.cursor()


        # 기존 search_youtube 테이블 드롭
        logger.info("youtube 검색 _ search_youtube_video 기존 테이블 삭제 중...")

        cursor.execute("DROP TABLE IF EXISTS playlist_schema.search_youtube_video;")

        # 기존 songs 테이블 드롭
        logger.info("spotify 추천곡 _ 기존 테이블 삭제 중...")
        cursor.execute("DROP TABLE IF EXISTS playlist_schema.spotify_recommend")

        logger.info("youtube 검색 _ search_youtube_video 새 테이블 생성 중...")
        # search_youtube 테이블 생성 (no는 SERIAL PK로 설정)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS playlist_schema.search_youtube_video (
                no SERIAL PRIMARY KEY,
                video_title VARCHAR(255),
                video_id VARCHAR(255)
            );
        """)

        logger.info("youtube 검색 _ search_youtube_video 새 테이블 생성 완료")


        # songs 테이블 생성 (no는 SERIAL PK로 설정)
        logger.info("spotify 추천곡 _ 새 테이블 생성 중...")
        create_table_query = """
        CREATE TABLE playlist_schema.spotify_recommend (
            no SERIAL PRIMARY KEY,
            title VARCHAR(256),
            link VARCHAR(256),
            cover_image VARCHAR(256)
        )
        """
        cursor.execute(create_table_query)
        logger.info("spotify 추천곡 _ 새 테이블 생성 완료")

        # youtube_songs 데이터프레임을 테이블에 삽입
        bulk_insert_table(cursor, conn, search_video_df, 'playlist_schema.search_youtube_video')
        logger.info("youtube 검색 _ search_youtube 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")

        # 데이터를 songs 테이블에 삽입
        for song in recommendations_data:
            insert_query = """
            INSERT INTO playlist_schema.spotify_recommend (title, link, cover_image)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (song['title'], song['link'], song['cover_image']))
        logger.info("spotify 추천곡 _ 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")

        #django_schema insert
        transform_schema(cursor)

        conn.commit()

    except Exception as e:
        # 예외 발생 시 롤백
        logger.error(f"추천곡 _ 데이터 로드 중 오류 발생: {e}")
        conn.rollback()

    finally:
        # 커서와 연결 닫기
        cursor.close()
        conn.close()
        logger.info("추천곡 _ 데이터베이스 연결이 종료되었습니다.")
    return


# Airflow DAG 정의
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
}

dag = DAG(
    'etl_dag_search_songs',  # DAG 이름
    default_args=default_args,
    description='ETL for recommend songs',
    schedule_interval= None,  # 추후 클릭 webhook 이벤트로 교체해야함
    catchup = False,
)


# Airflow Task 정의
def run_etl(**kwargs):
    # conf에서 song_title 받아오기
    song_title = kwargs['dag_run'].conf.get('input_value')
    
    if song_title:
        song_title = song_title
        search_video_df, recommendations_data = extract_data_from_site(song_title)
        load_data_to_db(search_video_df, recommendations_data)
    else:
        logger.error("song_title이 conf에서 제공되지 않았습니다.")

# DAG 안에서 Task 연결
etl_task = PythonOperator(
    task_id='etl_task_tracks',
    python_callable=run_etl,
    provide_context=True,  # dag_run을 context로 제공
    dag=dag,
)

etl_task

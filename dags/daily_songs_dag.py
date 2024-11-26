## daily song만 가져오는 부분으로 변경

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

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,  # 로그 레벨을 INFO로 설정
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def extract_data_from_site():
    """ Youtube에서 top10을 가져오는 함수 """
    youtube_client = YoutubeClient()
    daily_youtube_video_df, daily_youtube_playlist_df = youtube_client.daily_youtube()
    logger.info(f"youtube daily _ youtube 데일리 데이터를 성공적으로 가져왔습니다: {daily_youtube_video_df}, {daily_youtube_playlist_df}")
    
    """ Spotify에서 top10을 가져오는 함수 """
    spotify_client = SpotifyClient()
    top_tracks = spotify_client.get_top_10_tracks_from_playlist()
    logger.info(f"spotify today track _ 데이터를 성공적으로 가져왔습니다: {top_tracks}")
    
    return daily_youtube_video_df, top_tracks
    
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
        logger.info(f"youtube daily _ 테이블 {table_name}에 데이터 삽입 완료")
    except Exception as e:
        # 에러 발생 시 트랜잭션 롤백
        conn.rollback()
        print(f"youtube daily _ {table_name} 삽입 오류: {e}")
    finally:
        buffer.close()

def transform_schema(cursor):
    # daily_songs
    # 1. 테이블 삭제
    drop_table_query = "DROP TABLE IF EXISTS django_schema.daily_songs;"
    cursor.execute(drop_table_query)

    # 2. 테이블 생성
    create_table_query = """
    CREATE TABLE django_schema.daily_songs (
        no SERIAL PRIMARY KEY,
        song_title VARCHAR(255) NOT NULL,
        song_url VARCHAR(255) NOT NULL,
        thumbnail VARCHAR(255),
        platform VARCHAR(255) NOT NULL
    );
    """
    cursor.execute(create_table_query)

    # daily_youtube_video 데이터 삽입
    youtube_query = """
    INSERT INTO django_schema.daily_songs (song_title, song_url, thumbnail, platform)
    SELECT 
        video_title AS song_title,
        video_id AS song_url,
        CONCAT('https://img.youtube.com/vi/', video_id, '/0.jpg') AS thumbnail,
        'youtube' AS platform
    FROM playlist_schema.daily_youtube_video;
    """
    cursor.execute(youtube_query)

    # spotify_today_tracks 데이터 삽입
    spotify_query = """
    INSERT INTO django_schema.daily_songs (song_title, song_url, thumbnail, platform)
    SELECT 
        title AS song_title,
        link AS song_url,
        cover_image AS thumbnail,
        'spotify' AS platform
    FROM playlist_schema.spotify_today_tracks;
    """
    cursor.execute(spotify_query)
    return


def load_data_to_db(daily_youtube_video_df, top_tracks):
    """ 데이터베이스에 데이터 로드 """
    if daily_youtube_video_df.empty:
        logger.warning("youtube daily _ 빈 테이블이 있습니다.")
        return
    if not top_tracks:
        logger.warning("spotify today track _ 로드할 데이터가 없습니다.")
        return

    pg_hook = PostgresHook(postgres_conn_id='playlist')  # 연결 ID 사용
    conn_tmp = pg_hook.get_connection(pg_hook.postgres_conn_id)
    try:
        # 직접 psycopg2로 연결하고 인코딩을 설정
        conn = psycopg2.connect(
            host=conn_tmp.host,
            database=conn_tmp.schema,
            user=conn_tmp.login,
            password=conn_tmp.password,
            port=conn_tmp.port,
            client_encoding='UTF8'  # 인코딩 설정
        )
        cursor = conn.cursor()

        # 기존 songs 테이블 드롭
        logger.info("youtube daily _ daily_youtube 기존 테이블 삭제 중...")
        cursor.execute("DROP TABLE IF EXISTS playlist_schema.daily_youtube_video;")

        # 기존 songs 테이블 드롭
        logger.info("spotify today track _ 기존 테이블 삭제 중...")
        cursor.execute("DROP TABLE IF EXISTS playlist_schema.spotify_today_tracks")

        # songs 테이블 생성 (no는 SERIAL PK로 설정)
        logger.info("youtube daily _ daily_youtube 새 테이블 생성 중...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS playlist_schema.daily_youtube_video (
                no SERIAL PRIMARY KEY,
                video_title VARCHAR(255),
                video_id VARCHAR(255)
            );
        """)
        logger.info("youtube daily _ 새 테이블 생성 완료")

        # songs 테이블 생성 (no는 SERIAL PK로 설정)
        logger.info("spotify today track _ 새 테이블 생성 중...")
        create_table_query = """
        CREATE TABLE playlist_schema.spotify_today_tracks (
            no SERIAL PRIMARY KEY,
            title VARCHAR(256),
            link VARCHAR(256),
            cover_image VARCHAR(256)
        )
        """
        cursor.execute(create_table_query)
        logger.info("spotify today track _ 새 테이블 생성 완료")

        # 데이터를 songs 테이블에 삽입
        bulk_insert_table(cursor, conn, daily_youtube_video_df, 'playlist_schema.daily_youtube_video')
        logger.info("youtube daily _ 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")

        # 데이터를 songs 테이블에 삽입
        for song in top_tracks:
            insert_query = """
            INSERT INTO playlist_schema.spotify_today_tracks (title, link, cover_image)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (song['title'], song['link'], song['cover_image']))
        logger.info("spotify today track _ 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")

        transform_schema(cursor)
        conn.commit()
        
    except Exception as e:
        # 예외 발생 시 롤백
        logger.error(f"daily songs _ 데이터 로드 중 오류 발생: {e}")
        conn.rollback()

    finally:
        # 커서와 연결 닫기
        cursor.close()
        conn.close()
        logger.info("daily songs _ 데이터베이스 연결이 종료되었습니다.")
    return

# Airflow DAG 정의
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
}

dag = DAG(
    'etl_dag_daily_tracks',  # DAG 이름
    default_args=default_args,
    description='ETL for daily tracks',
    schedule_interval='0 0 * * *',  # 자정 
    catchup=False,  # 과거에 실행되지 않은 DAG를 실행하지 않도록 설정
)

# Airflow Task 정의
def run_etl():
    daily_youtube_video_df, top_tracks = extract_data_from_site()
    load_data_to_db(daily_youtube_video_df, top_tracks)

# DAG 안에서 Task 연결
etl_task = PythonOperator(
    task_id='etl_task_daily_tracks',
    python_callable=run_etl,
    dag=dag,
)

etl_task

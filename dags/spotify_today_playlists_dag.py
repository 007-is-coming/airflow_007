import os
import spotipy
from airflow.models import Variable
from spotipy.oauth2 import SpotifyOAuth
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
from spotify_class import SpotifyClient
import psycopg2
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,  # 로그 레벨을 INFO로 설정
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def extract_data_from_spotify():
    """ Spotify에서 추천곡을 가져오는 함수 """
    spotify_client = SpotifyClient()
    today_playlists_data = spotify_client.get_top_10_playlists()
    logger.info(f"spotify today playlist _ 데이터를 성공적으로 가져왔습니다: {today_playlists_data}")
    return today_playlists_data

def transform_schema(cursor):
    # daily_playlist
    # 1. 테이블 삭제
    drop_table_query = "DROP TABLE IF EXISTS django_schema.daily_playlists;"
    cursor.execute(drop_table_query)

    # 2. 테이블 생성
    create_table_query = """
    CREATE TABLE django_schema.daily_playlists (
        no SERIAL PRIMARY KEY,
        playlist_title VARCHAR(255) NOT NULL,
        playlist_url VARCHAR(255) NOT NULL,
        thumbnail VARCHAR(255),
        platform VARCHAR(255) NOT NULL
    );
    """
    cursor.execute(create_table_query)
    
    # 3. spotify_today_playlists 데이터 삽입
    spotify_query = """
    INSERT INTO django_schema.daily_playlists (playlist_title, playlist_url, thumbnail, platform)
    SELECT 
        title AS playlist_title,
        link AS playlist_url,
        cover_image AS thumbnail,
        'spotify' AS platform
    FROM playlist_schema.spotify_today_playlists;
    """
    cursor.execute(spotify_query)
    return

def load_data_to_db(today_playlists_data):
    """ 데이터베이스에 데이터 로드 """
    if not today_playlists_data:
        logger.warning("spotify today playlist _ 로드할 데이터가 없습니다.")
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
        logger.info("spotify today playlist _ 기존 테이블 삭제 중...")
        cursor.execute("DROP TABLE IF EXISTS playlist_schema.spotify_today_playlists")

        # songs 테이블 생성 (no는 SERIAL PK로 설정)
        logger.info("spotify today playlist _ 새 테이블 생성 중...")
        create_table_query = """
        CREATE TABLE playlist_schema.spotify_today_playlists (
            no SERIAL PRIMARY KEY,
            title VARCHAR(256),
            link VARCHAR(256),
            cover_image VARCHAR(256)
        )
        """
        cursor.execute(create_table_query)
        logger.info("spotify today playlist _ 새 테이블 생성 완료")

        # 데이터를 songs 테이블에 삽입
        for song in today_playlists_data:
            insert_query = """
            INSERT INTO playlist_schema.spotify_today_playlists (title, link, cover_image)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (song['title'], song['link'], song['cover_image']))


        #django_schema insert
        transform_schema(cursor)

        conn.commit()
        logger.info("spotify today playlist _ 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")

    except Exception as e:
        # 예외 발생 시 롤백
        logger.error(f"spotify today playlist _ 데이터 로드 중 오류 발생: {e}")
        conn.rollback()

    finally:
        # 커서와 연결 닫기
        cursor.close()
        conn.close() 
        logger.info("spotify today playlist _ 데이터베이스 연결이 종료되었습니다.")
    return

# Airflow DAG 정의
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
}

dag = DAG(
    'spotify_etl_dag_today_playlists',  # DAG 이름
    default_args=default_args,
    description='ETL for Spotify today playlists',
    schedule_interval='0 0 * * *',  # 매일 오후 12시 정각 실행 (CRON 표현식)
    catchup=False,  # 과거에 실행되지 않은 DAG를 실행하지 않도록 설정
)


# Airflow Task 정의
def run_etl():
    today_play_list_data = extract_data_from_spotify()
    load_data_to_db(today_play_list_data)

# DAG 안에서 Task 연결
etl_task = PythonOperator(
    task_id='spotify_etl_task_today_playlists',
    python_callable=run_etl,
    dag=dag,
)

etl_task

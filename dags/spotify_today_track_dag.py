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


def extract_data_from_spotify():
    """ Spotify에서 추천곡을 가져오는 함수 """
    spotify_client = SpotifyClient()
    top_tracks = spotify_client.get_top_10_tracks_from_playlist()
    return top_tracks

def load_data_to_db(top_tracks):
    """ 데이터베이스에 데이터 로드 """
    if not top_tracks:
        print("No data to load.")
        return

    pg_hook = PostgresHook(postgres_conn_id='playlist')  # 연결 ID 사용
    conn_tmp = pg_hook.get_connection(pg_hook.postgres_conn_id)
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
    cursor.execute("DROP TABLE IF EXISTS playlist_schema.spotify_today_tracks")

    # songs 테이블 생성 (no는 SERIAL PK로 설정)
    create_table_query = """
    CREATE TABLE playlist_schema.spotify_today_tracks (
        no SERIAL PRIMARY KEY,
        title VARCHAR(256),
        link VARCHAR(256),
        cover_image VARCHAR(256)
    )
    """
    cursor.execute(create_table_query)


    # 데이터를 songs 테이블에 삽입
    for song in top_tracks:
        insert_query = """
        INSERT INTO playlist_schema.spotify_today_tracks (title, link, cover_image)
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (song['title'], song['link'], song['cover_image']))

    conn.commit()
    cursor.close()
    conn.close()


# Airflow DAG 정의
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
}

dag = DAG(
    'spotify_etl_dag_today_track',  # DAG 이름
    default_args=default_args,
    description='ETL for Spotify Recommendations',
    schedule_interval='@daily',  # 추후 클릭 webhook 이벤트로 교체해야함
)

# Airflow Task 정의
def run_etl():
    top_tracks = extract_data_from_spotify()
    load_data_to_db(top_tracks)

# DAG 안에서 Task 연결
etl_task = PythonOperator(
    task_id='spotify_etl_task_today_track',
    python_callable=run_etl,
    dag=dag,
)

etl_task

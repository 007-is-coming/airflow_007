import os
import spotipy
from airflow.models import Variable
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
from youtube_class import YoutubeClient
import psycopg2
import pandas as pd
from io import StringIO
import csv

def extract_data_from_youtube():
    """ Spotify에서 추천곡을 가져오는 함수 """
    youtube_client = YoutubeClient()
    daily_youtube_video_df, daily_youtube_playlist_df = youtube_client.daily_youtube()
    return daily_youtube_video_df, daily_youtube_playlist_df

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
        print(f"테이블 {table_name}에 데이터 삽입 완료")
    except Exception as e:
        # 에러 발생 시 트랜잭션 롤백
        conn.rollback()
        print(f"{table_name} 삽입 오류: {e}")
    finally:
        buffer.close()

def load_data_to_db(daily_youtube_video_df, daily_youtube_playlist_df):
    """ 데이터베이스에 데이터 로드 """
    if not (daily_youtube_video_df or daily_youtube_playlist_df):
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
    cursor.execute("DROP TABLE IF EXISTS playlist_schema.daily_youtube_video;")
    cursor.execute("DROP TABLE IF EXISTS playlist_schema.daily_youtube_playlist;")

    # songs 테이블 생성 (no는 SERIAL PK로 설정)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlist_schema.daily_youtube_video (
            no SERIAL PRIMARY KEY,
            video_title VARCHAR(255),
            video_id VARCHAR(255)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlist_schema.daily_youtube_playlist (
            no SERIAL PRIMARY KEY,
            playlist_title VARCHAR(255),
            playlist_id VARCHAR(255)
        );
    """)

    # 데이터를 songs 테이블에 삽입
    bulk_insert_table(cursor, conn, daily_youtube_video_df, 'playlist_schema.daily_youtube_video')
    bulk_insert_table(cursor, conn, daily_youtube_playlist_df, 'playlist_schema.daily_youtube_playlist')

    conn.commit()
    cursor.close()
    conn.close()
    return 

# Airflow DAG 정의
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
}

dag = DAG(
    'youtube_etl_dag_daily_playlists',  # DAG 이름
    default_args=default_args,
    description='ETL for YouTube daily playlists',
    schedule_interval='@daily', 
)

# Airflow Task 정의
def run_etl():
    daily_youtube_video_df, daily_youtube_playlist_df = extract_data_from_youtube()
    load_data_to_db(daily_youtube_video_df, daily_youtube_playlist_df)

# DAG 안에서 Task 연결
etl_task = PythonOperator(
    task_id='youtube_etl_task_daily_playlists',
    python_callable=run_etl,
    dag=dag,
)

etl_task

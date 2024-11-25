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


def extract_data_from_spotify(song_title):
    """ Spotify에서 추천곡을 가져오는 함수 """
    spotify_client = SpotifyClient()
    recommendations_data = spotify_client.get_recommendations(song_title)
    return recommendations_data

def load_data_to_db(recommendations_data):
    """ 데이터베이스에 데이터 로드 """
    if not recommendations_data:
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
    cursor.execute("DROP TABLE IF EXISTS playlist_schema.spotify_recommend")

    # songs 테이블 생성 (no는 SERIAL PK로 설정)
    create_table_query = """
    CREATE TABLE playlist_schema.spotify_recommend (
        no SERIAL PRIMARY KEY,
        title VARCHAR(256),
        link VARCHAR(256),
        cover_image VARCHAR(256)
    )
    """
    cursor.execute(create_table_query)

    # 유튜브 추천 검색을 위한 return list
    recommand_list = []
    # 데이터를 songs 테이블에 삽입
    for song in recommendations_data:
        insert_query = """
        INSERT INTO playlist_schema.spotify_recommend (title, link, cover_image)
        VALUES (%s, %s, %s)
        """
        recommand_list.append(song)
        cursor.execute(insert_query, (song['title'], song['link'], song['cover_image']))

    conn.commit()
    cursor.close()
    conn.close()
    return recommand_list


# Airflow DAG 정의
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
}

dag = DAG(
    'spotify_etl_dag_recommend',  # DAG 이름
    default_args=default_args,
    description='ETL for Spotify Recommendations',
    schedule_interval='@daily',  # 추후 클릭 webhook 이벤트로 교체해야함
)

# Airflow Task 정의
def run_etl(song_title):
    recommendations_data = extract_data_from_spotify(song_title)
    load_data_to_db(recommendations_data)

# DAG 안에서 Task 연결
song_title = 'Shape of You'  # Django를 airflow Variable로 받아오기
etl_task = PythonOperator(
    task_id='spotify_etl_task_recommend',
    python_callable=run_etl,
    op_args=[song_title],
    dag=dag,
)

etl_task

def run_etl(**kwargs):
    # 사용자 입력 값 가져오기
    song_title = kwargs['dag_run'].conf.get('song_title', 'Default Song')
    recommendations_data = extract_data_from_spotify(song_title)
    load_data_to_db(recommendations_data)

dag = DAG(
    'spotify_etl_dag_recommend',
    default_args=default_args,
    description='ETL for Spotify Recommendations',
    schedule_interval=None,  # 트리거로만 실행
)

etl_task = PythonOperator(
    task_id='spotify_etl_task_recommend',
    python_callable=run_etl,
    provide_context=True,  # DAG 컨텍스트 전달
    dag=dag,
)


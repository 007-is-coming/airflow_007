# airflow_007

# 옥탑방 플리 🎧

**`3차 7팀 ‘007**’ **| 권찬송, 김윤정, 이민지, 전수민, 송기웅, 최혜림**`

## I. 프로젝트 배경 및 목표

<aside>

### **🔍 기존 음원 사이트의 음악 추천 기능의 한계**

- 하나의 음원 사이트 내에서만 누적된 데이터를 기준으로 노래를 추천 받을 수 있음
- 내가 원하는 노래 한 곡에 대해 여러가지 사이트에서 추천하는 노래를 찾기 힘듦

### **👤 다양한 플랫폼의 데이터를 활용한 통합 추천**

- 유튜브와 스포티파이의 강점을 결합하여 사용자에게 **`한 플랫폼을 넘어선 폭넓은 추천 서비스`** 제공
- 각 플랫폼의 특성(커버곡, 전문 큐레이팅 등)을 반영한 **`최적화된 추천 경험`** 제공
</aside>

## II. 활용 기술 및 프로젝트 구조

<aside>

| TASK | 활용 기술 | 비고 |
| --- | --- | --- |
| Data Collection | Python, SQL | **`Spotify API`**, **`Youtube API`**사용 |
| Data Preprocessing | Python, SQL | API 호출 후 데이터베이스에 맞게 변경 |
| Data Warehouse(DB) | On-premise  | **`Postgre`** API를 통해 가지고 온 데이터 적재 |
| Visualization | Django | **`Web Page`** 검색 및 추천 결과 출력 |
| Team Management | Notion, Discord, Github, VSCode | **`Notion`**프로젝트 회의 기록, 프로젝트 보고서 작성
**`Discord`** 프로젝트 회의 및 실시간 공유
**`Github`** 프로젝트 결과물 실시간 업데이트
**`VSCode`** live share를 통해 실시간으로 코드 공유 및 협업 |

### ⚙ System Architecture

![[프로그래머스] 3차 7팀 프로젝트 개발 아키텍처 (1).jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/29dd0948-7b38-443b-af5a-c6bc908226ab/54afbed8-5a11-4f98-a17b-e18f17c51313/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4_3%EC%B0%A8_7%ED%8C%80_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EA%B0%9C%EB%B0%9C_%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98_(1).jpg)

</aside>

## III. 결과물

### **📊 Web Page Demonstration Video**

<aside>

- **`Demonstration video`**
    
    [화면 기록 2024-11-27 13.01.27.mov](https://prod-files-secure.s3.us-west-2.amazonaws.com/29dd0948-7b38-443b-af5a-c6bc908226ab/2b6e86d3-adff-4c0a-ab1c-9dbaf98174d5/%E1%84%92%E1%85%AA%E1%84%86%E1%85%A7%E1%86%AB_%E1%84%80%E1%85%B5%E1%84%85%E1%85%A9%E1%86%A8_2024-11-27_13.01.27.mov)
    
</aside>

### **📊 Web Page Screenshot**

<aside>

- **`Main`**
    
    ![home_page.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/29dd0948-7b38-443b-af5a-c6bc908226ab/064d60a5-b6a5-454b-8027-d5a4ffa432de/a1e7ce11-c21d-48cc-a483-50dabbb83c75.png)
    
- **`Youtube`**
    
    ![result_page.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/29dd0948-7b38-443b-af5a-c6bc908226ab/de0c8b14-cb2e-4567-b397-678b3d20cd58/180db265-7c3b-4705-a0fd-1894bbffd4d3.png)
    
- **`Spotify`**
    
    ![result_page2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/29dd0948-7b38-443b-af5a-c6bc908226ab/55e98ff0-d0b6-4358-9afe-e3fa75e5de0d/00d040a6-0865-4897-81ad-c4b5ced7792f.png)
    
- **`Play`**
    
    ![palyer.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/29dd0948-7b38-443b-af5a-c6bc908226ab/8ff25999-3dc0-42ff-83d1-db6ab89776b6/3f7e012e-4f8e-4db5-b799-b6c03cf0f992.png)
    
</aside>

### **📊 Presentation**

<aside>

https://www.canva.com/design/DAGXjmUbIOk/qWKyaSuho3Reux-sdDO_Vw/view

</aside>

## IV. 프로젝트 세부 내용

<aside>

### **🔶 ERD**

![3.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/29dd0948-7b38-443b-af5a-c6bc908226ab/6062b889-cf0e-4942-8daf-b189404c3208/4e21d835-5db4-43bf-b9d2-1c2cf53790db.png)

### **⚒ 개발 단계별 TASK**

- **Step1. 데이터 수집 및 전처리**
    - **데이터 수집**
        
        
        | Data Name | Source | Update Date | Description |
        | --- | --- | --- | --- |
        | spotify_playlist | spotify api | trigger (django) 발생 시  | 검색어인 노래를 포함하는 playlist |
        | spotify_recommend | spotify api | trigger (django) 발생 시 | 검색어인 노래를 기준으로 recommend된 노래 |
        | search_youtube_playlist | youtube api | trigger (django) 발생 시 | 검색어인 노래를 포함하는 playlist (music 검색어) |
        | search_youtube_video | youtube api | trigger (django) 발생 시  | 검색어인 노래를 기준으로 recommend된 video (music 검색어) |
        | spotify_today_tracks | spotify api | 매일 자정 | 매일 global top 50에서 상위 10개의 노래  |
        | spotify_today_playlists | spotify api | 매일 자정 | 매일 ‘top’을 포함하는 상위 10개의 playlist |
        | daily_youtube_video | youtube api | 매일 자정 | 매일 global top video 중 상위 10개 (music 검색어) |
    - **데이터 전처리**
        
        
        | Data Set | 기존 Column | 전처리 후 Column | 전처리 내용 |
        | --- | --- | --- | --- |
        | spotify_playlist / search_youtube_playlist  | no, title, link, cover_image / no, playlist_title, playlist_id, playlist_thumbnail | no, playlist_title, playlist_url, thumbnail, platform | youtube와 spotify에서 가지고온 데이터를 하나의 테이블로 통합 |
        | spotify_recommend / search_youtube_video | no, title, link, cover_image / no, video_title, video_id | no, song_title, song_url, thumbnail, platform | youtube와 spotify에서 가지고온 데이터를 하나의 테이블로 통합 |
        | spotify_today_tracks / daily_youtube_video | no, title, link, cover_image /  no, video_title, video_id | no, song_title, song_url, thumbnail, platform | youtube와 spotify에서 가지고온 데이터를 하나의 테이블로 통합 |
- **Step2. 데이터 적재**
    
    📋**Airflow를 활용한 Dag 사용으로 데이터 자동 적재**
    
    > **`📈 playlist_schema 및 django_schema 데이터 적재`**
    > 
    > - [**`daily_songs_dag.py`**] `Spotify 오늘의 Top 10 track 및 Youtube 오늘의 Top 10 video (매일 자정 갱신)`
    >     
    >     ```python
    >     ## daily song만 가져오는 부분으로 변경
    >     
    >     import os
    >     import spotipy
    >     from airflow.models import Variable
    >     from airflow import DAG
    >     from airflow.operators.python import PythonOperator
    >     from airflow.providers.postgres.hooks.postgres import PostgresHook
    >     from datetime import datetime, timedelta
    >     from youtube_class import YoutubeClient
    >     from spotify_class import SpotifyClient
    >     import psycopg2
    >     import pandas as pd
    >     from io import StringIO
    >     import csv
    >     import logging
    >     
    >     # 로깅 설정
    >     logging.basicConfig(
    >         level=logging.INFO,  # 로그 레벨을 INFO로 설정
    >         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    >     )
    >     logger = logging.getLogger(__name__)
    >     
    >     def extract_data_from_site():
    >         """ Youtube에서 top10을 가져오는 함수 """
    >         youtube_client = YoutubeClient()
    >         daily_youtube_video_df, daily_youtube_playlist_df = youtube_client.daily_youtube()
    >         logger.info(f"youtube daily _ youtube 데일리 데이터를 성공적으로 가져왔습니다: {daily_youtube_video_df}, {daily_youtube_playlist_df}")
    >         
    >         """ Spotify에서 top10을 가져오는 함수 """
    >         spotify_client = SpotifyClient()
    >         top_tracks = spotify_client.get_top_10_tracks_from_playlist()
    >         logger.info(f"spotify today track _ 데이터를 성공적으로 가져왔습니다: {top_tracks}")
    >         
    >         return daily_youtube_video_df, top_tracks
    >         
    >     def bulk_insert_table(cursor, conn, df, table_name):
    >         """
    >         데이터프레임을 PostgreSQL 테이블에 COPY 명령으로 빠르게 삽입.
    >         """
    >         # 데이터프레임을 CSV 형식으로 메모리에 저장
    >         buffer = StringIO()
    >         df.to_csv(buffer, index=False, header=False, quotechar='"', quoting=csv.QUOTE_ALL)
    >         buffer.seek(0)
    >     
    >         try:
    >             # COPY 명령 실행
    >             cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", buffer)
    >             logger.info(f"youtube daily _ 테이블 {table_name}에 데이터 삽입 완료")
    >         except Exception as e:
    >             # 에러 발생 시 트랜잭션 롤백
    >             conn.rollback()
    >             print(f"youtube daily _ {table_name} 삽입 오류: {e}")
    >         finally:
    >             buffer.close()
    >     
    >     def transform_schema(cursor):
    >         # daily_songs
    >         # 1. 테이블 삭제
    >         drop_table_query = "DROP TABLE IF EXISTS django_schema.daily_songs;"
    >         cursor.execute(drop_table_query)
    >     
    >         # 2. 테이블 생성
    >         create_table_query = """
    >         CREATE TABLE django_schema.daily_songs (
    >             no SERIAL PRIMARY KEY,
    >             song_title VARCHAR(255) NOT NULL,
    >             song_url VARCHAR(255) NOT NULL,
    >             thumbnail VARCHAR(255),
    >             platform VARCHAR(255) NOT NULL
    >         );
    >         """
    >         cursor.execute(create_table_query)
    >     
    >         # daily_youtube_video 데이터 삽입
    >         youtube_query = """
    >         INSERT INTO django_schema.daily_songs (song_title, song_url, thumbnail, platform)
    >         SELECT 
    >             video_title AS song_title,
    >             video_id AS song_url,
    >             CONCAT('https://img.youtube.com/vi/', video_id, '/0.jpg') AS thumbnail,
    >             'youtube' AS platform
    >         FROM playlist_schema.daily_youtube_video;
    >         """
    >         cursor.execute(youtube_query)
    >     
    >         # spotify_today_tracks 데이터 삽입
    >         spotify_query = """
    >         INSERT INTO django_schema.daily_songs (song_title, song_url, thumbnail, platform)
    >         SELECT 
    >             title AS song_title,
    >             link AS song_url,
    >             cover_image AS thumbnail,
    >             'spotify' AS platform
    >         FROM playlist_schema.spotify_today_tracks;
    >         """
    >         cursor.execute(spotify_query)
    >         return
    >     
    >     def load_data_to_db(daily_youtube_video_df, top_tracks):
    >         """ 데이터베이스에 데이터 로드 """
    >         if daily_youtube_video_df.empty:
    >             logger.warning("youtube daily _ 빈 테이블이 있습니다.")
    >             return
    >         if not top_tracks:
    >             logger.warning("spotify today track _ 로드할 데이터가 없습니다.")
    >             return
    >     
    >         pg_hook = PostgresHook(postgres_conn_id='playlist')  # 연결 ID 사용
    >         conn_tmp = pg_hook.get_connection(pg_hook.postgres_conn_id)
    >         try:
    >             # 직접 psycopg2로 연결하고 인코딩을 설정
    >             conn = psycopg2.connect(
    >                 host=conn_tmp.host,
    >                 database=conn_tmp.schema,
    >                 user=conn_tmp.login,
    >                 password=conn_tmp.password,
    >                 port=conn_tmp.port,
    >                 client_encoding='UTF8'  # 인코딩 설정
    >             )
    >             cursor = conn.cursor()
    >     
    >             # 기존 songs 테이블 드롭
    >             logger.info("youtube daily _ daily_youtube 기존 테이블 삭제 중...")
    >             cursor.execute("DROP TABLE IF EXISTS playlist_schema.daily_youtube_video;")
    >     
    >             # 기존 songs 테이블 드롭
    >             logger.info("spotify today track _ 기존 테이블 삭제 중...")
    >             cursor.execute("DROP TABLE IF EXISTS playlist_schema.spotify_today_tracks")
    >     
    >             # songs 테이블 생성 (no는 SERIAL PK로 설정)
    >             logger.info("youtube daily _ daily_youtube 새 테이블 생성 중...")
    >             cursor.execute("""
    >                 CREATE TABLE IF NOT EXISTS playlist_schema.daily_youtube_video (
    >                     no SERIAL PRIMARY KEY,
    >                     video_title VARCHAR(255),
    >                     video_id VARCHAR(255)
    >                 );
    >             """)
    >             logger.info("youtube daily _ 새 테이블 생성 완료")
    >     
    >             # songs 테이블 생성 (no는 SERIAL PK로 설정)
    >             logger.info("spotify today track _ 새 테이블 생성 중...")
    >             create_table_query = """
    >             CREATE TABLE playlist_schema.spotify_today_tracks (
    >                 no SERIAL PRIMARY KEY,
    >                 title VARCHAR(256),
    >                 link VARCHAR(256),
    >                 cover_image VARCHAR(256)
    >             )
    >             """
    >             cursor.execute(create_table_query)
    >             logger.info("spotify today track _ 새 테이블 생성 완료")
    >     
    >             # 데이터를 songs 테이블에 삽입
    >             bulk_insert_table(cursor, conn, daily_youtube_video_df, 'playlist_schema.daily_youtube_video')
    >             logger.info("youtube daily _ 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")
    >     
    >             # 데이터를 songs 테이블에 삽입
    >             for song in top_tracks:
    >                 insert_query = """
    >                 INSERT INTO playlist_schema.spotify_today_tracks (title, link, cover_image)
    >                 VALUES (%s, %s, %s)
    >                 """
    >                 cursor.execute(insert_query, (song['title'], song['link'], song['cover_image']))
    >             logger.info("spotify today track _ 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")
    >     
    >             transform_schema(cursor)
    >             conn.commit()
    >             
    >         except Exception as e:
    >             # 예외 발생 시 롤백
    >             logger.error(f"daily songs _ 데이터 로드 중 오류 발생: {e}")
    >             conn.rollback()
    >     
    >         finally:
    >             # 커서와 연결 닫기
    >             cursor.close()
    >             conn.close()
    >             logger.info("daily songs _ 데이터베이스 연결이 종료되었습니다.")
    >         return
    >     
    >     # Airflow DAG 정의
    >     default_args = {
    >         'owner': 'airflow',
    >         'retries': 1,
    >         'retry_delay': timedelta(minutes=5),
    >         'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
    >     }
    >     
    >     dag = DAG(
    >         'etl_dag_daily_tracks',  # DAG 이름
    >         default_args=default_args,
    >         description='ETL for daily tracks',
    >         schedule_interval='0 0 * * *',  # 자정 
    >         catchup=False,  # 과거에 실행되지 않은 DAG를 실행하지 않도록 설정
    >     )
    >     
    >     # Airflow Task 정의
    >     def run_etl():
    >         daily_youtube_video_df, top_tracks = extract_data_from_site()
    >         load_data_to_db(daily_youtube_video_df, top_tracks)
    >     
    >     # DAG 안에서 Task 연결
    >     etl_task = PythonOperator(
    >         task_id='etl_task_daily_tracks',
    >         python_callable=run_etl,
    >         dag=dag,
    >     )
    >     
    >     etl_task
    >     ```
    >     
    > - [**`spotify_today_playlists_dag.py`**] `Spotify의 playlist 중 top 키워드를 포함하는 playlist 중 상위 10개 (매일 자정 갱신)`
    >     
    >     ```python
    >     import os
    >     import spotipy
    >     from airflow.models import Variable
    >     from spotipy.oauth2 import SpotifyOAuth
    >     from airflow import DAG
    >     from airflow.operators.python import PythonOperator
    >     from airflow.providers.postgres.hooks.postgres import PostgresHook
    >     from datetime import datetime, timedelta
    >     from spotify_class import SpotifyClient
    >     import psycopg2
    >     import logging
    >     
    >     # 로깅 설정
    >     logging.basicConfig(
    >         level=logging.INFO,  # 로그 레벨을 INFO로 설정
    >         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    >     )
    >     logger = logging.getLogger(__name__)
    >     
    >     def extract_data_from_spotify():
    >         """ Spotify에서 추천곡을 가져오는 함수 """
    >         spotify_client = SpotifyClient()
    >         today_playlists_data = spotify_client.get_top_10_playlists()
    >         logger.info(f"spotify today playlist _ 데이터를 성공적으로 가져왔습니다: {today_playlists_data}")
    >         return today_playlists_data
    >     
    >     def transform_schema(cursor):
    >         # daily_playlist
    >         # 1. 테이블 삭제
    >         drop_table_query = "DROP TABLE IF EXISTS django_schema.daily_playlists;"
    >         cursor.execute(drop_table_query)
    >     
    >         # 2. 테이블 생성
    >         create_table_query = """
    >         CREATE TABLE django_schema.daily_playlists (
    >             no SERIAL PRIMARY KEY,
    >             playlist_title VARCHAR(255) NOT NULL,
    >             playlist_url VARCHAR(255) NOT NULL,
    >             thumbnail VARCHAR(255),
    >             platform VARCHAR(255) NOT NULL
    >         );
    >         """
    >         cursor.execute(create_table_query)
    >         
    >         # 3. spotify_today_playlists 데이터 삽입
    >         spotify_query = """
    >         INSERT INTO django_schema.daily_playlists (playlist_title, playlist_url, thumbnail, platform)
    >         SELECT 
    >             title AS playlist_title,
    >             link AS playlist_url,
    >             cover_image AS thumbnail,
    >             'spotify' AS platform
    >         FROM playlist_schema.spotify_today_playlists;
    >         """
    >         cursor.execute(spotify_query)
    >         return
    >     
    >     def load_data_to_db(today_playlists_data):
    >         """ 데이터베이스에 데이터 로드 """
    >         if not today_playlists_data:
    >             logger.warning("spotify today playlist _ 로드할 데이터가 없습니다.")
    >             return
    >     
    >         pg_hook = PostgresHook(postgres_conn_id='playlist')  # 연결 ID 사용
    >         conn_tmp = pg_hook.get_connection(pg_hook.postgres_conn_id)
    >         try:
    >             # 직접 psycopg2로 연결하고 인코딩을 설정
    >             conn = psycopg2.connect(
    >                 host=conn_tmp.host,
    >                 database=conn_tmp.schema,
    >                 user=conn_tmp.login,
    >                 password=conn_tmp.password,
    >                 port=conn_tmp.port,
    >                 client_encoding='UTF8'  # 인코딩 설정
    >             )
    >             cursor = conn.cursor()
    >     
    >             # 기존 songs 테이블 드롭
    >             logger.info("spotify today playlist _ 기존 테이블 삭제 중...")
    >             cursor.execute("DROP TABLE IF EXISTS playlist_schema.spotify_today_playlists")
    >     
    >             # songs 테이블 생성 (no는 SERIAL PK로 설정)
    >             logger.info("spotify today playlist _ 새 테이블 생성 중...")
    >             create_table_query = """
    >             CREATE TABLE playlist_schema.spotify_today_playlists (
    >                 no SERIAL PRIMARY KEY,
    >                 title VARCHAR(256),
    >                 link VARCHAR(256),
    >                 cover_image VARCHAR(256)
    >             )
    >             """
    >             cursor.execute(create_table_query)
    >             logger.info("spotify today playlist _ 새 테이블 생성 완료")
    >     
    >             # 데이터를 songs 테이블에 삽입
    >             for song in today_playlists_data:
    >                 insert_query = """
    >                 INSERT INTO playlist_schema.spotify_today_playlists (title, link, cover_image)
    >                 VALUES (%s, %s, %s)
    >                 """
    >                 cursor.execute(insert_query, (song['title'], song['link'], song['cover_image']))
    >     
    >             #django_schema insert
    >             transform_schema(cursor)
    >     
    >             conn.commit()
    >             logger.info("spotify today playlist _ 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")
    >     
    >         except Exception as e:
    >             # 예외 발생 시 롤백
    >             logger.error(f"spotify today playlist _ 데이터 로드 중 오류 발생: {e}")
    >             conn.rollback()
    >     
    >         finally:
    >             # 커서와 연결 닫기
    >             cursor.close()
    >             conn.close() 
    >             logger.info("spotify today playlist _ 데이터베이스 연결이 종료되었습니다.")
    >         return
    >     
    >     # Airflow DAG 정의
    >     default_args = {
    >         'owner': 'airflow',
    >         'retries': 1,
    >         'retry_delay': timedelta(minutes=5),
    >         'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
    >     }
    >     
    >     dag = DAG(
    >         'spotify_etl_dag_today_playlists',  # DAG 이름
    >         default_args=default_args,
    >         description='ETL for Spotify today playlists',
    >         schedule_interval='0 0 * * *',  # 매일 오후 12시 정각 실행 (CRON 표현식)
    >         catchup=False,  # 과거에 실행되지 않은 DAG를 실행하지 않도록 설정
    >     )
    >     
    >     # Airflow Task 정의
    >     def run_etl():
    >         today_play_list_data = extract_data_from_spotify()
    >         load_data_to_db(today_play_list_data)
    >     
    >     # DAG 안에서 Task 연결
    >     etl_task = PythonOperator(
    >         task_id='spotify_etl_task_today_playlists',
    >         python_callable=run_etl,
    >         dag=dag,
    >     )
    >     
    >     etl_task
    >     ```
    >     
    > - [**`songs_dag.py`**] `검색어 기반 Spotify 추천 상위 10개 track / Spotify 추천 목록 10개 기반 Youtube 상위 video (Django input trigger 갱신)`
    >     
    >     ```python
    >     import os
    >     import spotipy
    >     from airflow.models import Variable
    >     from airflow import DAG
    >     from airflow.operators.python import PythonOperator
    >     from airflow.providers.postgres.hooks.postgres import PostgresHook
    >     from datetime import datetime, timedelta
    >     from youtube_class import YoutubeClient
    >     from spotify_class import SpotifyClient
    >     import psycopg2
    >     import pandas as pd
    >     from io import StringIO
    >     import csv
    >     import logging
    >     
    >     logging.basicConfig(
    >         level=logging.INFO,  # 로그 레벨을 INFO로 설정
    >         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    >     )
    >     logger = logging.getLogger(__name__)
    >     
    >     def extract_data_from_site(song_title):
    >         """ Spotify에서 추천곡을 가져오는 함수 """
    >         spotify_client = SpotifyClient()
    >         recommendations_data, youtube_recommendations_data = spotify_client.get_recommendations(song_title)
    >         logger.info(f"spotify 추천곡 _ 데이터를 성공적으로 가져왔습니다: {recommendations_data}")
    >     
    >         """ Youtube에서 추천곡을 가져오는 함수 """
    >         youtube_client = YoutubeClient()
    >         search_video_df = youtube_client.search_youtube(youtube_recommendations_data)
    >         logger.info(f"youtube 추천곡 _ 데이터를 성공적으로 가져왔습니다: {search_video_df}")
    >         
    >         return search_video_df, recommendations_data
    >     
    >     def bulk_insert_table(cursor, conn, df, table_name):
    >         """
    >         데이터프레임을 PostgreSQL 테이블에 COPY 명령으로 빠르게 삽입.
    >         """
    >         # 데이터프레임을 CSV 형식으로 메모리에 저장
    >         buffer = StringIO()
    >         df.to_csv(buffer, index=False, header=False, quotechar='"', quoting=csv.QUOTE_ALL)
    >         buffer.seek(0)
    >     
    >         try:
    >             # COPY 명령 실행
    >             cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", buffer)
    >             logger.info(f"youtube 검색 _ 테이블 {table_name}에 데이터 삽입 완료")
    >         except Exception as e:
    >             # 에러 발생 시 트랜잭션 롤백
    >             conn.rollback()
    >             logger.error(f"youtube 검색 _ {table_name} 삽입 오류: {e}")
    >         finally:
    >             buffer.close()
    >     
    >     def transform_schema(cursor):
    >         # search_songs
    >         # 1. 테이블 삭제
    >         logger.info(f" search songs : 데이터를 삭제합니다.")
    >         drop_table_query = "DROP TABLE IF EXISTS django_schema.search_songs;"
    >         cursor.execute(drop_table_query)
    >         
    >         # 2. 테이블 생성
    >         create_table_query = """
    >         CREATE TABLE django_schema.search_songs (
    >             no SERIAL PRIMARY KEY,
    >             song_title VARCHAR(255) NOT NULL,
    >             song_url VARCHAR(255) NOT NULL,
    >             thumbnail VARCHAR(255),
    >             platform VARCHAR(255) NOT NULL
    >         );
    >         """
    >         cursor.execute(create_table_query)
    >         logger.info(" search_songs _ 새 테이블 생성 완료")
    >     
    >         
    >         # 3. search_youtube_video 데이터를 search_songs에 삽입
    >         youtube_query = """
    >         INSERT INTO django_schema.search_songs (song_title, song_url, thumbnail, platform)
    >         SELECT 
    >             video_title AS song_title,
    >             video_id AS song_url,
    >             CONCAT('https://img.youtube.com/vi/', video_id, '/0.jpg') AS thumbnail,
    >             'youtube' AS platform
    >         FROM playlist_schema.search_youtube_video;
    >         """
    >         cursor.execute(youtube_query)
    >     
    >         # 4. spotify_recommend 데이터를 search_songs에 삽입
    >         spotify_query = """
    >         INSERT INTO django_schema.search_songs (song_title, song_url, thumbnail, platform)
    >         SELECT 
    >             title AS song_title,
    >             link AS song_url,
    >             cover_image AS thumbnail,
    >             'spotify' AS platform
    >         FROM playlist_schema.spotify_recommend;
    >         """
    >         cursor.execute(spotify_query)
    >         logger.info(f" search songs : 데이터가 삽입 되었습니다.")
    >     
    >         return
    >     
    >     def load_data_to_db(search_video_df, recommendations_data):
    >         """ 데이터베이스에 데이터 로드 """
    >         if search_video_df.empty:
    >             logger.warning("youtube 검색 _ 테이블에 빈 테이블이 있습니다.")
    >             return
    >         if not recommendations_data:
    >             logger.warning("spotify 추천곡 _ 로드할 데이터가 없습니다.")
    >             return
    >     
    >         pg_hook = PostgresHook(postgres_conn_id='playlist')  # 연결 ID 사용
    >         conn_tmp = pg_hook.get_connection(pg_hook.postgres_conn_id)
    >         # 직접 psycopg2로 연결하고 인코딩을 설정
    >         try:
    >             conn = psycopg2.connect(
    >                 host=conn_tmp.host,
    >                 database=conn_tmp.schema,
    >                 user=conn_tmp.login,
    >                 password=conn_tmp.password,
    >                 port=conn_tmp.port,
    >                 client_encoding='UTF8'  # 인코딩 설정
    >             )
    >             cursor = conn.cursor()
    >     
    >             # 기존 search_youtube 테이블 드롭
    >             logger.info("youtube 검색 _ search_youtube_video 기존 테이블 삭제 중...")
    >     
    >             cursor.execute("DROP TABLE IF EXISTS playlist_schema.search_youtube_video;")
    >     
    >             # 기존 songs 테이블 드롭
    >             logger.info("spotify 추천곡 _ 기존 테이블 삭제 중...")
    >             cursor.execute("DROP TABLE IF EXISTS playlist_schema.spotify_recommend")
    >     
    >             logger.info("youtube 검색 _ search_youtube_video 새 테이블 생성 중...")
    >             # search_youtube 테이블 생성 (no는 SERIAL PK로 설정)
    >             cursor.execute("""
    >                 CREATE TABLE IF NOT EXISTS playlist_schema.search_youtube_video (
    >                     no SERIAL PRIMARY KEY,
    >                     video_title VARCHAR(255),
    >                     video_id VARCHAR(255)
    >                 );
    >             """)
    >     
    >             logger.info("youtube 검색 _ search_youtube_video 새 테이블 생성 완료")
    >     
    >             # songs 테이블 생성 (no는 SERIAL PK로 설정)
    >             logger.info("spotify 추천곡 _ 새 테이블 생성 중...")
    >             create_table_query = """
    >             CREATE TABLE playlist_schema.spotify_recommend (
    >                 no SERIAL PRIMARY KEY,
    >                 title VARCHAR(256),
    >                 link VARCHAR(256),
    >                 cover_image VARCHAR(256)
    >             )
    >             """
    >             cursor.execute(create_table_query)
    >             logger.info("spotify 추천곡 _ 새 테이블 생성 완료")
    >     
    >             # youtube_songs 데이터프레임을 테이블에 삽입
    >             bulk_insert_table(cursor, conn, search_video_df, 'playlist_schema.search_youtube_video')
    >             logger.info("youtube 검색 _ search_youtube 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")
    >     
    >             # 데이터를 songs 테이블에 삽입
    >             for song in recommendations_data:
    >                 insert_query = """
    >                 INSERT INTO playlist_schema.spotify_recommend (title, link, cover_image)
    >                 VALUES (%s, %s, %s)
    >                 """
    >                 cursor.execute(insert_query, (song['title'], song['link'], song['cover_image']))
    >             logger.info("spotify 추천곡 _ 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")
    >     
    >             #django_schema insert
    >             transform_schema(cursor)
    >     
    >             conn.commit()
    >     
    >         except Exception as e:
    >             # 예외 발생 시 롤백
    >             logger.error(f"추천곡 _ 데이터 로드 중 오류 발생: {e}")
    >             conn.rollback()
    >     
    >         finally:
    >             # 커서와 연결 닫기
    >             cursor.close()
    >             conn.close()
    >             logger.info("추천곡 _ 데이터베이스 연결이 종료되었습니다.")
    >         return
    >     
    >     # Airflow DAG 정의
    >     default_args = {
    >         'owner': 'airflow',
    >         'retries': 1,
    >         'retry_delay': timedelta(minutes=5),
    >         'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
    >     }
    >     
    >     dag = DAG(
    >         'etl_dag_search_songs',  # DAG 이름
    >         default_args=default_args,
    >         description='ETL for recommend songs',
    >         schedule_interval= None,  # 추후 클릭 webhook 이벤트로 교체해야함
    >         catchup = False,
    >     )
    >     
    >     # Airflow Task 정의
    >     def run_etl(**kwargs):
    >         # conf에서 song_title 받아오기
    >         song_title = kwargs['dag_run'].conf.get('input_value')
    >         
    >         if song_title:
    >             song_title = song_title
    >             search_video_df, recommendations_data = extract_data_from_site(song_title)
    >             load_data_to_db(search_video_df, recommendations_data)
    >         else:
    >             logger.error("song_title이 conf에서 제공되지 않았습니다.")
    >     
    >     # DAG 안에서 Task 연결
    >     etl_task = PythonOperator(
    >         task_id='etl_task_tracks',
    >         python_callable=run_etl,
    >         provide_context=True,  # dag_run을 context로 제공
    >         dag=dag,
    >     )
    >     
    >     etl_task
    >     
    >     ```
    >     
    > - [**`playlist_dag.py`**] `검색어 기반 Spotify 추천 상위 10개 playlist / 검색어 기반 Youtube playlist 중 상위 10개 playlist (Django input trigger 갱신)`
    >     
    >     ```python
    >     import os
    >     import spotipy
    >     from airflow.models import Variable
    >     from airflow import DAG
    >     from airflow.operators.python import PythonOperator
    >     from airflow.providers.postgres.hooks.postgres import PostgresHook
    >     from datetime import datetime, timedelta
    >     from youtube_class import YoutubeClient
    >     from spotify_class import SpotifyClient
    >     import psycopg2
    >     import pandas as pd
    >     from io import StringIO
    >     import csv
    >     import logging
    >     
    >     logging.basicConfig(
    >         level=logging.INFO,  # 로그 레벨을 INFO로 설정
    >         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    >     )
    >     logger = logging.getLogger(__name__)
    >     
    >     def extract_data_from_site(song_title):
    >         
    >         """spotify에서 playlist를 가지고 오는 함수"""
    >         spotify_client = SpotifyClient()
    >         playlist_data = spotify_client.find_playlists_by_song(song_title)
    >         logger.info(f"spotify playlist _ 데이터를 성공적으로 가져왔습니다: {playlist_data}")
    >     
    >         """ youtube에서 playlist를 가져오는 함수 """
    >         youtube_client = YoutubeClient()
    >         search_playlist_df = youtube_client.search_youtube_playlist(song_title + " music")
    >         logger.info(f"youtube 검색 _ 데이터를 성공적으로 가져왔습니다: {search_playlist_df}")
    >     
    >         return search_playlist_df, playlist_data
    >     
    >     def bulk_insert_table(cursor, conn, df, table_name):
    >         """
    >         데이터프레임을 PostgreSQL 테이블에 COPY 명령으로 빠르게 삽입.
    >         """
    >         # 데이터프레임을 CSV 형식으로 메모리에 저장
    >         buffer = StringIO()
    >         df.to_csv(buffer, index=False, header=False, quotechar='"', quoting=csv.QUOTE_ALL)
    >         buffer.seek(0)
    >     
    >         try:
    >             # COPY 명령 실행
    >             cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", buffer)
    >             logger.info(f"youtube 검색 _ 테이블 {table_name}에 데이터 삽입 완료")
    >         except Exception as e:
    >             # 에러 발생 시 트랜잭션 롤백
    >             conn.rollback()
    >             logger.error(f"youtube 검색 _ {table_name} 삽입 오류: {e}")
    >         finally:
    >             buffer.close()
    >     
    >     def transform_schema(cursor):
    >         # search_playlist
    >         # 1. 테이블 삭제
    >         drop_table_query = "DROP TABLE IF EXISTS django_schema.search_playlist;"
    >         cursor.execute(drop_table_query)
    >     
    >         # 2. 테이블 생성
    >         create_table_query = """
    >         CREATE TABLE django_schema.search_playlist (
    >             no SERIAL PRIMARY KEY,
    >             playlist_title VARCHAR(255) NOT NULL,
    >             playlist_url VARCHAR(255) NOT NULL,
    >             thumbnail VARCHAR(255),
    >             platform VARCHAR(255) NOT NULL
    >         );
    >         """
    >         cursor.execute(create_table_query)
    >     
    >         # 3. search_youtube_video 데이터를 search_songs에 삽입
    >         youtube_query = """
    >         INSERT INTO django_schema.search_playlist (playlist_title, playlist_url, thumbnail, platform)
    >         SELECT 
    >             playlist_title AS playlist_title,
    >             playlist_id AS playlist_url,
    >             playlist_thumbnail AS thumbnail,
    >             'youtube' AS platform
    >         FROM playlist_schema.search_youtube_playlist;
    >         """
    >         cursor.execute(youtube_query)
    >     
    >         # 4. spotify_recommend 데이터를 search_songs에 삽입
    >         spotify_query = """
    >         INSERT INTO django_schema.search_playlist (playlist_title, playlist_url, thumbnail, platform)
    >         SELECT 
    >             title AS playlist_title,
    >             link AS playlist_url,
    >             cover_image AS thumbnail,
    >             'spotify' AS platform
    >         FROM playlist_schema.spotify_playlist;
    >         """
    >         cursor.execute(spotify_query)
    >         return
    >     
    >     def load_data_to_db(search_playlist_df, playlist_data):
    >         """ 데이터베이스에 데이터 로드 """
    >         if search_playlist_df.empty:
    >             logger.warning("youtube 검색 _ 테이블에 빈 테이블이 있습니다.")
    >             return
    >         if not playlist_data:
    >             logger.warning("spotify playlist _ 로드할 데이터가 없습니다.")
    >             return
    >     
    >         pg_hook = PostgresHook(postgres_conn_id='playlist')  # 연결 ID 사용
    >         conn_tmp = pg_hook.get_connection(pg_hook.postgres_conn_id)
    >         # 직접 psycopg2로 연결하고 인코딩을 설정
    >         try:
    >             conn = psycopg2.connect(
    >                 host=conn_tmp.host,
    >                 database=conn_tmp.schema,
    >                 user=conn_tmp.login,
    >                 password=conn_tmp.password,
    >                 port=conn_tmp.port,
    >                 client_encoding='UTF8'  # 인코딩 설정
    >             )
    >             cursor = conn.cursor()
    >     
    >             # 기존 search_youtube 테이블 드롭
    >             logger.info("youtube 검색 _ search_youtube 기존 테이블 삭제 중...")
    >             cursor.execute("DROP TABLE IF EXISTS playlist_schema.search_youtube_playlist;")
    >     
    >             # 기존 playlists 테이블 드롭
    >             logger.info("spotify playlist _ 기존 테이블 삭제 중...")
    >             cursor.execute("DROP TABLE IF EXISTS playlist_schema.spotify_playlist")
    >     
    >             logger.info("youtube 검색 _ search_youtube_playlist 새 테이블 생성 중...")
    >             # search_youtube 테이블 생성 (no는 SERIAL PK로 설정)
    >             cursor.execute("""
    >                 CREATE TABLE IF NOT EXISTS playlist_schema.search_youtube_playlist (
    >                     no SERIAL PRIMARY KEY,
    >                     playlist_title VARCHAR(255),
    >                     playlist_id VARCHAR(255),
    >                     playlist_thumbnail VARCHAR(255)
    >                 );
    >             """)
    >             logger.info("youtube 검색 _ search_youtube_playlist 새 테이블 생성 완료")
    >             
    >             # playlists 테이블 생성 (no는 SERIAL PK로 설정)
    >             logger.info("spotify playlist _ 새 테이블 생성 중...")
    >             cursor.execute("""
    >             CREATE TABLE playlist_schema.spotify_playlist (
    >                 no SERIAL PRIMARY KEY,
    >                 title VARCHAR(256),
    >                 link VARCHAR(256),
    >                 cover_image VARCHAR(256)
    >                 );
    >             """)
    >             logger.info("spotify playlist _ 새 테이블 생성 완료")
    >     
    >             # youtube 데이터프레임을 테이블에 삽입
    >             bulk_insert_table(cursor, conn, search_playlist_df, 'playlist_schema.search_youtube_playlist')
    >             logger.info("youtube 검색 _ search_youtube_playlist 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")
    >             
    >             # 데이터를 playlists 테이블에 삽입
    >             for playlist in playlist_data:
    >                 insert_query = """
    >                 INSERT INTO playlist_schema.spotify_playlist (title, link, cover_image)
    >                 VALUES (%s, %s, %s)
    >                 """
    >                 cursor.execute(insert_query, (playlist['title'], playlist['link'], playlist['cover_image']))
    >             logger.info("spotify playlist _ 데이터가 성공적으로 데이터베이스에 삽입되었습니다.")
    >     
    >             #django schema insert
    >             transform_schema(cursor)
    >     
    >             conn.commit()
    >             
    >         except Exception as e:
    >             # 예외 발생 시 롤백
    >             logger.error(f"playlist _ 데이터 로드 중 오류 발생: {e}")
    >             conn.rollback()
    >     
    >         finally:
    >             # 커서와 연결 닫기
    >             cursor.close()
    >             conn.close()
    >             logger.info("playlist _ 데이터베이스 연결이 종료되었습니다.")
    >         return
    >     
    >     # Airflow DAG 정의
    >     default_args = {
    >         'owner': 'airflow',
    >         'retries': 1,
    >         'retry_delay': timedelta(minutes=5),
    >         'start_date': datetime(2023, 11, 22),  # 원하는 시작 날짜 설정
    >     }
    >     
    >     dag = DAG(
    >         'etl_dag_playlist',  # DAG 이름
    >         default_args=default_args,
    >         description='ETL for recommend Playlists',
    >         schedule_interval=None,  # 추후 클릭 webhook 이벤트로 교체해야함
    >         catchup = False,
    >     )
    >     
    >     # Airflow Task 정의
    >     def run_etl(**kwargs):
    >         # conf에서 song_title 받아오기
    >         song_title = kwargs['dag_run'].conf.get('input_value')
    >         
    >         if song_title:
    >             song_title = song_title
    >             search_playlist_df, playlist_data = extract_data_from_site(song_title)
    >             load_data_to_db(search_playlist_df, playlist_data)
    >         else:
    >             logger.error("song_title이 conf에서 제공되지 않았습니다.")
    >     
    >     # DAG 안에서 Task 연결
    >     etl_task = PythonOperator(
    >         task_id='etl_task_playlist',
    >         python_callable=run_etl,
    >         provide_context=True,  # dag_run을 context로 제공
    >         dag=dag,
    >     )
    >     
    >     etl_task
    >     ```
    >     
    > - [**`spotify_class.py`**] `spotify api 사용을 위한 class`
    >     
    >     ```python
    >     import os
    >     import spotipy
    >     from airflow.models import Variable
    >     from spotipy.oauth2 import SpotifyClientCredentials
    >     from airflow import DAG
    >     from airflow.operators.python import PythonOperator
    >     from airflow.providers.postgres.hooks.postgres import PostgresHook
    >     from datetime import datetime, timedelta
    >     import requests
    >     import base64
    >     
    >     class SpotifyClient:
    >         def __init__(self):
    >             """ 환경 변수 가져오기 """
    >             client_id = Variable.get("CLIENT_ID")
    >             client_secret = Variable.get("CLIENT_SECRET")
    >     
    >             # Spotipy initialization
    >             self.scope = "playlist-read-private playlist-read-collaborative"
    >             self.sp = spotipy.Spotify(
    >                 auth_manager=SpotifyClientCredentials(
    >                     client_id=client_id,
    >                     client_secret=client_secret,
    >                 )
    >             )
    >             
    >         def get_recommendations(self, song_title):
    >             """ 추천곡을 가져오는 함수 """
    >             # 노래 검색
    >             results = self.sp.search(q=song_title, type='track', limit=1)
    >             
    >             if not results['tracks']['items']:
    >                 print("No track found with that name.")
    >                 return []
    >             
    >             track = results['tracks']['items'][0]
    >             print(f"Found track: {track['name']} by {track['artists'][0]['name']}")
    >     
    >             # 추천 곡 받기
    >             recommendations = self.sp.recommendations(seed_tracks=[track['id']], limit=20)
    >             
    >             recommendations_data = []
    >             youtube_recommendations_data = []
    >             for rec in recommendations['tracks']:
    >                 album_cover_url = rec['album']['images'][0]['url']
    >                 song_info = {
    >                     "title": rec['name'],
    >                     "link": rec['external_urls']['spotify'],
    >                     "cover_image": album_cover_url
    >                 }
    >                 if len(recommendations_data) < 10:
    >                     recommendations_data.append(song_info)
    >                 else:
    >                     youtube_recommendations_data.append(rec['name'])
    >     
    >             return recommendations_data, youtube_recommendations_data
    >     
    >         def find_playlists_by_song(self, song_title):
    >             """ 노래 제목을 입력받아 해당 노래가 포함된 플레이리스트를 찾는 함수 """
    >             # 노래 검색
    >             results = self.sp.search(q=song_title, type='track', limit=10)
    >             
    >             if not results['tracks']['items']:
    >                 print("No track found with that name.")
    >                 return []
    >             
    >             track = results['tracks']['items'][0]
    >             print(f"Found track: {track['name']} by {track['artists'][0]['name']}")
    >     
    >             # 해당 트랙을 포함한 플레이리스트 검색
    >             playlists = self.sp.search(q=track['name'], type='playlist', limit=10)
    >             
    >             if not playlists['playlists']['items']:
    >                 print("No playlists found containing this song.")
    >                 return []
    >             
    >             playlist_data = []
    >             for playlist in playlists['playlists']['items']:
    >                 playlist_name = playlist['name']
    >                 playlist_url = playlist['external_urls']['spotify']
    >                 playlist_cover_url = playlist['images'][0]['url'] if playlist['images'] else 'No image available'
    >                 playlist_info = {
    >                     "title": playlist_name,
    >                     "link": playlist_url,
    >                     "cover_image": playlist_cover_url
    >                 }
    >                 playlist_data.append(playlist_info)
    >                 
    >             return playlist_data
    >         
    >         def get_top_10_playlists(self):
    >             # 'Top'이라는 키워드로 플레이리스트 검색
    >             results = self.sp.search(q="Top", type='playlist', limit=10)
    >     
    >             if not results['playlists']['items']:
    >                 print("No playlists found.")
    >                 return
    >     
    >             print(f"Top 10 playlists:")
    >             today_playlists_data = []
    >             for idx, playlist in enumerate(results['playlists']['items'], 1):
    >                 playlist_name = playlist['name']
    >                 playlist_url = playlist['external_urls']['spotify']
    >                 playlist_cover_url = playlist['images'][0]['url'] if playlist['images'] else 'No image available'
    >                 playlist_info = {
    >                     "title": playlist_name,
    >                     "link": playlist_url,
    >                     "cover_image": playlist_cover_url
    >                 }
    >                 today_playlists_data.append(playlist_info)
    >                 
    >             return today_playlists_data
    >         
    >         def get_top_10_tracks_from_playlist(self):
    >             # 'Global Top 50' 플레이리스트 ID
    >             global_top_50_playlist_id = '37i9dQZEVXbMDoHDwVN2tF'  # 이 ID는 Spotify Global Top 50 플레이리스트의 ID입니다.
    >             
    >             # 플레이리스트에서 트랙 가져오기
    >             results = self.sp.playlist_tracks(global_top_50_playlist_id, limit=10)
    >     
    >             if not results['items']:
    >                 print("No tracks found in the playlist.")
    >                 return
    >     
    >             top_songs = []
    >             for item in results['items']:
    >                 track = item['track']  # 트랙 정보는 'track' 키 아래에 존재합니다.
    >                 album_cover_url = track['album']['images'][0]['url'] if track['album']['images'] else 'No image available'
    >                 song_info = {
    >                     "title": track['name'],
    >                     "link": track['external_urls']['spotify'],
    >                     "cover_image": album_cover_url
    >                 }
    >                 top_songs.append(song_info)
    >     
    >             return top_songs
    >     ```
    >     
    > - [**`youtube_class.py`**] `youtube api 사용을 위한 class`
    >     
    >     ```python
    >     import requests
    >     import pandas as pd
    >     from airflow.models import Variable
    >     from spotipy.oauth2 import SpotifyClientCredentials
    >     from airflow import DAG
    >     from airflow.operators.python import PythonOperator
    >     from airflow.providers.postgres.hooks.postgres import PostgresHook
    >     import html
    >     
    >     # YouTube Data API 설정
    >     
    >     class YoutubeClient:
    >         def __init__(self):
    >             self.API_KEY = Variable.get("API_KEY") # airflow Var
    >             self.SEARCH_URL = Variable.get("SEARCH_URL")
    >             self.BASE_URL = Variable.get("BASE_URL")
    >     
    >         def search_youtube_playlist(self, song_title, max_results=10):
    >             params = {
    >                 'key': self.API_KEY,
    >                 'q': song_title,
    >                 'type': 'playlist',
    >                 'part': 'snippet',
    >                 'maxResults': max_results
    >             }
    >             response = requests.get(self.SEARCH_URL, params=params)
    >     
    >             if response.status_code != 200:
    >                 print(f"Error: {response.status_code}, {response.text}")
    >                 return pd.DataFrame()  # 빈 DataFrame 반환
    >     
    >             data = response.json()
    >             playlists = []
    >             for idx, item in enumerate(data.get('items', []), 1):
    >                 title = item['snippet']['title']
    >                 title = html.unescape(title)
    >                 playlist_id = item['id']['playlistId']
    >                 thumbnails = item["snippet"].get("thumbnails", {})
    >                 thumbnail_url = thumbnails.get("medium", {}).get("url", "")  # 썸네일 URL 가져오기
    >                 playlists.append({
    >                     "no": idx,
    >                     "playlist_title": item["snippet"]["title"],
    >                     "playlist_id": playlist_id,
    >                     'playlist_thumbnail': thumbnail_url
    >                 })
    >     
    >             return pd.DataFrame(playlists)
    >         
    >         def search_youtube(self, youtube_recommendations_data, max_results=10):
    >             """
    >             특정 노래 제목으로 동영상과 플레이리스트를 
    >             10개씩 검색하여 DataFrame으로 반환하는 함수.
    >             """
    >             #spotify 노래 받아오기
    >             videos = []
    >             for search_keyword in youtube_recommendations_data:
    >                 #spotify 노래 기준 search
    >                 params = {
    >                     'key': self.API_KEY,
    >                     'q': search_keyword,
    >                     'type': 'video',
    >                     'part': 'snippet',
    >                     'maxResults': 1
    >                 }
    >                 response = requests.get(self.SEARCH_URL, params=params)
    >     
    >                 if response.status_code != 200:
    >                     print(f"Error: {response.status_code}, {response.text}")
    >                     return pd.DataFrame()  # 빈 DataFrame 반환
    >                 
    >                 data = response.json()
    >                 
    >                 title = data.get('items')[0]['snippet']['title']
    >                 title = html.unescape(title)
    >                 video_id = data.get('items')[0]['id']['videoId']
    >                 idx = len(videos) + 1
    >                 videos.append({'no': idx, 'video_title': title, 'video_id': video_id})
    >     
    >             return pd.DataFrame(videos)
    >     
    >         def daily_youtube(self):
    >             # 1. '음악' 카테고리의 인기 비디오 가져오기
    >             url = f"{self.BASE_URL}/videos"
    >             params = {
    >                 "part": "snippet,statistics",
    >                 "chart": "mostPopular",
    >                 "videoCategoryId": "10",  # 음악 카테고리
    >                 "maxResults": 10,  # Top 10
    >                 "key": self.API_KEY,
    >             }
    >     
    >             response = requests.get(url, params=params)
    >     
    >             if response.status_code == 200:
    >                 data = response.json()
    >                 videos = data.get("items", [])
    >                 video_list = []
    >     
    >                 # 2. 비디오 정보를 정리
    >                 for idx, video in enumerate(videos, 1):
    >                     video_id = video["id"]
    >                     # video_id가 문자열인지 확인
    >                     if isinstance(video_id, str):
    >                         video_id = video["id"]  # id가 문자열이라면 바로 사용
    >                     elif isinstance(video_id, dict):
    >                         video_id = video_id.get("videoId", "")  # 딕셔너리에서 videoId 추출
    >                     video_list.append({
    >                         "no": idx,
    >                         "video_title": video["snippet"]["title"],
    >                         "video_id": video_id
    >                     })
    >     
    >             else:
    >                 print(f"API 요청 실패: {response.status_code}, {response.text}")
    >                 return []
    >     
    >             # 1. '음악' 카테고리의 인기 플레이리스트 가져오기
    >             url = f"{self.BASE_URL}/search"
    >             params = {
    >                 "part": "snippet",
    >                 "type": "playlist",  # 플레이리스트만 검색
    >                 "maxResults": 10,  # Top 10
    >                 "key": self.API_KEY,
    >             }
    >     
    >             response = requests.get(url, params=params)
    >     
    >             if response.status_code == 200:
    >                 data = response.json()
    >                 playlists = data.get("items", [])
    >                 playlist_list = []
    >     
    >                 # 2. 플레이리스트 정보를 정리
    >                 for idx, playlist in enumerate(playlists, 1):
    >                     playlist_id = playlist["id"].get("playlistId", "")
    >                     thumbnails = playlist["snippet"].get("thumbnails", {})
    >                     thumbnail_url = thumbnails.get("medium", {}).get("url", "")  # 썸네일 URL 가져오기
    >     
    >                     playlist_list.append({
    >                         "no": idx,
    >                         "playlist_title": playlist["snippet"]["title"],
    >                         "playlist_id": playlist_id,
    >                         'playlist_thumbnail': thumbnail_url
    >                     })
    >     
    >                 return pd.DataFrame(video_list), pd.DataFrame(playlist_list)
    >             else:
    >                 print(f"API 요청 실패: {response.status_code}, {response.text}")
    >                 return []
    >     
    >     ```
    >     
    
    📋**데이터베이스 설정 및 적재**
    
    **[Schema] playlist_schema**
    
    > **`📈 video, track, playlist 데이터 적재`**
    > 
    > - [**`spotify_today_tracks`**] `spotify 오늘의 Top 10 track`
    >     
    >     ```sql
    >     CREATE TABLE playlist_schema.spotify_today_tracks (
    >     	no	serial	NOT NULL,
    >     	title	VARCHAR(255)	NOT NULL,
    >     	link	VARCHAR(255)	NOT NULL,
    >     	cover_image	VARCHAR(255)	NOT NULL
    >     );
    >     ```
    >     
    > - [**`spotify_today_playlists`**] `spotify 오늘의 top playlist`
    >     
    >     ```sql
    >     CREATE TABLE playlist_schema.spotify_today_playlists (
    >     	no	serial	NOT NULL,
    >     	title	VARCHAR(255)	NOT NULL,
    >     	link	VARCHAR(255)	NOT NULL,
    >     	cover_image	VARCHAR(255)	NOT NULL
    >     );
    >     ```
    >     
    > - [**`spotify_playlist`**] `검색어 기준 spotify 추천 playlist`
    >     
    >     ```sql
    >     CREATE TABLE playlist_schema.spotify_playlist (
    >     	no	serial	NOT NULL,
    >     	title	VARCHAR(255)	NOT NULL,
    >     	link	VARCHAR(255)	NOT NULL,
    >     	cover_image	VARCHAR(255)	NOT NULL
    >     );
    >     ```
    >     
    > - [**`spotify_recommend`**] `검색어 기준 spotify 추천 track`
    >     
    >     ```sql
    >     CREATE TABLE playlist_schema.spotify_recommend (
    >     	no	serial	NOT NULL,
    >     	title	VARCHAR(255)	NOT NULL,
    >     	cover_image	VARCHAR(255)	NOT NULL
    >     );
    >     ```
    >     
    > - [**`daily_youtube_video`**] `youtube 오늘의 top video`
    >     
    >     ```sql
    >     CREATE TABLE playlist_schema.daily_youtube_video (
    >     	no	serial	NOT NULL,
    >     	video_title	VARCHAR(255)	NOT NULL,
    >     	video_id	VARCHAR(255)	NOT NULL
    >     );
    >     ```
    >     
    > - [**`search_youtube_playlist`**] `검색어 기준 youtube 추천 playlist`
    >     
    >     ```sql
    >     CREATE TABLE playlist_schema.search_youtube_playlist (
    >     	no	serial	NOT NULL,
    >     	playlist_title	VARCHAR(255)	NOT NULL,
    >     	playlist_id	VARCHAR(255)	NOT NULL,
    >     	playlist_thumbnail	VARCHAR(255)	NOT NULL
    >     );
    >     ```
    >     
    > - [**`search_youtube_video`**] `검색어 기준 youtube 추천 video`
    >     
    >     ```sql
    >     CREATE TABLE playlist_schema.search_youtube_video (
    >     	no	serial	NOT NULL,
    >     	video_title	VARCHAR(255)	NOT NULL,
    >     	video_id	VARCHAR(255)	NOT NULL
    >     );
    >     ```
    >     
    
    **[Schema] django_schema**
    
    > **`📉 Production DB`**
    > 
    > - [**`search_songs`**] `검색어 기준 spotify 추천 track 및 youtube 추천 video 통합`
    >     
    >     ```sql
    >     CREATE TABLE django_schema.search_songs (
    >     	no	serial	NOT NULL,
    >     	song_title	VARCHAR(255)	NOT NULL,
    >     	song_url	VARCHAR(255)	NOT NULL,
    >     	thumbnail	VARCHAR(255)	NOT NULL,
    >     	platform	ENUM	NOT NULL
    >     );
    >     ```
    >     
    > - [**`search_playlist`**] `검색어 기준 spotify 및 youtube 추천 playlist 통합`
    >     
    >     ```sql
    >     CREATE TABLE django_schema.search_playlist (
    >     	no	serial	NOT NULL,
    >     	playlist_title	VARCHAR(255)	NOT NULL,
    >     	playlist_url	VARCHAR(255)	NOT NULL,
    >     	thumbnail	VARCHAR(255)	NOT NULL,
    >     	platform	ENUM	NOT NULL
    >     );
    >     ```
    >     
    > - [**`daily_songs`**] `spotify 오늘의 top 10 및 youtube 오늘의 top video 통합`
    >     
    >     ```sql
    >     CREATE TABLE django_schema.daily_songs (
    >     	no	serial	NOT NULL,
    >     	song_title	VARCHAR(255)	NOT NULL,
    >     	song_url	VARCHAR(255)	NOT NULL,
    >     	thumbnail	VARCHAR(255)	NOT NULL,
    >     	platform	ENUM	NOT NULL
    >     );
    >     ```
    >     
    > - [**`daily_playlists`**] `spotify 및 youtube 오늘의 top playlist 통합`
    >     
    >     ```sql
    >     CREATE TABLE django_schema.daily_playlists (
    >     	no	serial	NOT NULL,
    >     	playlist_title	VARCHAR(255)	NOT NULL,
    >     	playlist_url	VARCHAR(255)	NOT NULL,
    >     	thumbnail	VARCHAR(255)	NOT NULL,
    >     	platform	ENUM	NOT NULL
    >     );
    >     ```
    >     
- **Step3. 데이터 시각화 및 Django (Web UI)**
    
    **📊 오늘의 Youtube, Spotify 추천 곡 및 플레이리스트 제공**
    
    **📊 노래 검색 기반의 Youtube, Spotifiy 추천 곡 및 플레이리스트 제공**
    
    **백엔드 (Model, View)**
    
    > **`📑 Model`**
    > 
    > - [**`models.py`**]
    >     
    >     ```python
    >     # 플랫폼 선택지 ENUM 정의
    >     class PlatformEnum(models.TextChoices):
    >     YOUTUBE = 'youtube', 'YouTube'
    >     SPOTIFY = 'spotify', 'Spotify'
    >     
    >     # DailySongs 모델
    >     class DailySongs(models.Model):
    >     no = models.AutoField(primary_key=True)
    >     song_title = models.CharField(max_length=255, verbose_name="Song Title")
    >     song_url = models.URLField(max_length=255, verbose_name="Song URL")
    >     thumbnail = models.URLField(max_length=255, null=True, blank=True, verbose_name="Thumbnail")
    >     platform = models.CharField(
    >     max_length=10,
    >     choices=PlatformEnum.choices,
    >     verbose_name="Platform",
    >     )
    >     
    >     class Meta:
    >         db_table = 'daily_songs'
    >         verbose_name = 'Daily Song'
    >         verbose_name_plural = 'Daily Songs'
    >     
    >     # DailyPlaylists 모델
    >     class DailyPlaylists(models.Model):
    >     no = models.AutoField(primary_key=True)  # 기본 키를 'no'로 설정
    >     playlist_title = models.CharField(max_length=252, verbose_name="Playlist Title")
    >     playlist_url = models.URLField(max_length=255, verbose_name="Playlist URL")
    >     thumbnail = models.URLField(max_length=255, null=True, blank=True, verbose_name="Thumbnail")
    >     platform = models.CharField(
    >     max_length=10,
    >     choices=PlatformEnum.choices,
    >     verbose_name="Platform",
    >     )
    >     class Meta:
    >         db_table = 'daily_playlists'
    >         verbose_name = 'Daily Playlist'
    >         verbose_name_plural = 'Daily Playlists'
    >     
    >     # SearchSongs 모델
    >     class SearchSongs(models.Model):
    >     no = models.AutoField(primary_key=True)  # 기본 키를 'no'로 설정
    >     song_title = models.CharField(max_length=255, verbose_name="Song Title")
    >     song_url = models.URLField(max_length=255, verbose_name="Song URL")
    >     thumbnail = models.URLField(max_length=255, null=True, blank=True, verbose_name="Thumbnail")
    >     platform = models.CharField(
    >     max_length=10,
    >     choices=PlatformEnum.choices,
    >     verbose_name="Platform",
    >     )
    >     class Meta:
    >         db_table = 'search_songs'
    >         verbose_name = 'Search Song'
    >         verbose_name_plural = 'Search Songs'
    >     
    >     # SearchPlaylist 모델
    >     class SearchPlaylist(models.Model):
    >     no = models.AutoField(primary_key=True)  # 기본 키를 'no'로 설정
    >     playlist_title = models.CharField(max_length=252, verbose_name="Playlist Title")
    >     playlist_url = models.URLField(max_length=255, verbose_name="Playlist URL")
    >     thumbnail = models.URLField(max_length=255, null=True, blank=True, verbose_name="Thumbnail")
    >     platform = models.CharField(
    >     max_length=10,
    >     choices=PlatformEnum.choices,
    >     verbose_name="Platform",
    >     )
    >     
    >     class Meta:
    >         db_table = 'search_playlist'
    >         verbose_name = 'Search Playlist'
    >         verbose_name_plural = 'Search Playlists'
    >     ```
    >     
    > 
    >         `PostgreSQL db 모델링 및 데이터 마이그레이션`
    > 
    > **`📑 View`**
    > 
    > - [**`views.py`**]
    >     
    >     ```python
    >     from django.shortcuts import render, redirect
    >     from django.http import HttpResponse, JsonResponse
    >     from django.views.decorators.csrf import csrf_exempt
    >     from .models import DailySongs, DailyPlaylists, SearchSongs, SearchPlaylist
    >     import time
    >     
    >     def index(request):
    >         daily_songs = DailySongs.objects.all()
    >         daily_playlists = DailyPlaylists.objects.all()
    >     
    >         print(f"Daily Songs count: {daily_songs.count()}")
    >         print(f"Daily Playlists count: {daily_playlists.count()}")
    >     
    >         for song in daily_songs:
    >             print(f"Song: {song.song_title}, URL: {song.song_url}")
    >     
    >         for playlist in daily_playlists:
    >             playlist.playlist_url = playlist.playlist_url.replace("playlist", "embed/playlist")
    >     
    >         context = {
    >             'daily_songs': daily_songs,
    >             'daily_playlists': daily_playlists,
    >         }
    >         return render(request, 'search/index.html', context)
    >     
    >     import requests
    >     from requests.auth import HTTPBasicAuth
    >     
    >     @csrf_exempt
    >     def trigger_airflow_dag(request):
    >         if request.method == "POST":
    >             input_value = request.POST.get("input_value")
    >             platform = request.POST.get("platform")
    >     
    >             if not input_value:
    >                 return JsonResponse({"error": "검색어를 입력해주세요!"}, status=400)
    >             
    >             if not platform:
    >                 return JsonResponse({"error": "검색 플랫폼을 선택해주세요!"}, status=400)
    >     
    >             # 세션에 저장
    >             request.session['platform'] = platform
    >             request.session['input_value'] = input_value
    >     
    >             # airflow_url = "http://airflow_007-airflow-webserver:8080/api/v1/dags/etl_dag_search_songs/dagRuns"
    >             # airflow_url_playlist = "http://airflow_007-airflow-webserver:8080/api/v1/dags/etl_dag_playlist/dagRuns"
    >             airflow_url = "http://localhost:8080/api/v1/dags/example_trigger_dag/dagRuns"
    >             username = 'airflow'
    >             password = 'airflow'
    >     
    >             payload = {
    >                 "conf": {"input_value": input_value}
    >             }
    >     
    >             headers = {
    >                 'Content-Type': 'application/json',
    >                 'Accept': 'application/json',
    >             }
    >     
    >             try:
    >                 # response = requests.post(airflow_url, json=payload, headers=headers, auth=HTTPBasicAuth(username, password))
    >                 # response_play = requests.post(airflow_url_playlist, json=payload, headers=headers, auth=HTTPBasicAuth(username, password))
    >                 response = requests.post(airflow_url, json=payload, headers=headers, auth=HTTPBasicAuth(username, password))
    >                 if response.status_code == 200 : #and response_play.status_code == 200:
    >                     time.sleep(5)
    >                     # 트리거 성공 후 결과 페이지로 리디렉션
    >                     return redirect('result')  # 'result'는 결과 페이지의 URL 이름
    >                 else:
    >                     return JsonResponse({"error": response.json()}, status=response.status_code)
    >             except Exception as e:
    >                 return JsonResponse({"error": str(e)}, status=500)
    >     
    >         return JsonResponse({"error": "Invalid request method"}, status=405)
    >     
    >     def result(request):    
    >         # 세션에서 정보 가져오기
    >         platform = request.session.get('platform', None)
    >         input_value = request.session.get('input_value', None)
    >     
    >         # 모든 데이터 가져오기
    >         search_songs = SearchSongs.objects.all()
    >         search_playlists = SearchPlaylist.objects.all()
    >     
    >         # Spotify URL 변환
    >         for song in search_songs:
    >             if song.platform == "spotify" and "track" in song.song_url:
    >                 song.transformed_url = song.song_url.replace("track", "embed/track")
    >             else:
    >                 song.transformed_url = song.song_url
    >     
    >         for playlist in search_playlists:
    >             if playlist.platform == "spotify" and "playlist" in playlist.playlist_url:
    >                 playlist.playlist_url = playlist.playlist_url.replace("playlist", "embed/playlist")
    >     
    >         # 템플릿으로 데이터 전달
    >         context = {
    >             'search_songs': search_songs,
    >             'search_playlists': search_playlists,
    >             'platform': platform,  # 플랫폼 정보 전달
    >             'input_value': input_value,
    >         }
    >         return render(request, 'search/result.html', context)
    >     ```
    >     
    > 
    >          `DB에서 오늘의 추천 곡 및 플레이리스트를 가져와 index.html에 렌더링`
    > 
    >          `사용자 검색 요청을 받아 Airflow DAG 호출`
    > 
    >          `검색어와 플랫폼에 따른 결과 데이터를 가져와 result.html에 렌더링`
    > 
    > **`📑 Django REST API`**
    > 
    > - [**`Django view 로직`**]
    >     
    >     ```html
    >     <!-- 검색어 입력 받기: frontend -->
    >     <form method="post" action="/trigger-dag/">
    >         {% csrf_token %}
    >         <input type="text" name="input_value" placeholder="Enter value">
    >         <button type="submit">Trigger DAG</button>
    >     </form>
    >     ```
    >     
    >     ```python
    >     # 입력받은 검색어 Airflow로 보내기: Beckend
    >     import requests
    >     from django.http import JsonResponse
    >     from requests.auth import HTTPBasicAuth
    >     
    >     def trigger_airflow_dag(request):
    >         if request.method == "POST":
    >             input_value = request.POST.get("input_value")  # form-data에서 key값에 해당하는 값 가져오기
    >             
    >             if not input_value:
    >                 return JsonResponse({"error": "No input_value provided"}, status=400)
    >     
    >             airflow_url = "http://localhost:8080/api/v1/dags/example_trigger_dag/dagRuns" # 요청 url
    >             username = 'your_username'
    >             password = 'your_password'
    >     
    >             payload = {
    >                 "conf": {"input_value": input_value}
    >             }
    >     
    >             headers = {
    >                 'Content-Type': 'application/json',  # 요청 본문 형식을 JSON으로 설정
    >                 'Accept': 'application/json',         # 응답 형식도 JSON으로 설정
    >             }
    >     
    >             try:
    >                 response = requests.post(airflow_url, json=payload, headers=headers, auth=HTTPBasicAuth(username, password))
    >     
    >                 if response.status_code == 200:
    >                     return JsonResponse({"message": "DAG triggered successfully!"})
    >                 else:
    >                     return JsonResponse({"error": response.json()}, status=response.status_code)
    >             except Exception as e:
    >                 return JsonResponse({"error": str(e)}, status=500)
    >     
    >         return JsonResponse({"error": "Invalid request method"}, status=405)
    >     
    >     ```
    >     
    > 
    >         `사용자 입력값을 Django 웹앱에서 수집`
    > 
    >         `Django가 Airflow REST API 호출: 입력값을 Airflow의 DAG로 전달`
    > 
    > - [**`Airflow DAG`**]
    >     
    >     ```python
    >     # DAG 예시
    >     from airflow import DAG
    >     from airflow.operators.python import PythonOperator
    >     from datetime import datetime
    >     
    >     def process_input_value(**kwargs):
    >         # Django에서 전달한 conf 값 가져오기
    >         input_value = kwargs['dag_run'].conf.get('input_value', 'default_value')  # 기본값 설정
    >         print(f"Received input value: {input_value}")
    >         # 처리 로직 추가
    >         return f"Processed input value: {input_value}"
    >     
    >     # DAG 정의
    >     with DAG(
    >         dag_id="example_trigger_dag",
    >         start_date=datetime(2023, 1, 1),  # DAG 시작일 설정
    >         schedule_interval=None,  # 스케줄 없음 (외부 트리거로만 실행)
    >         catchup=False,  # 백필 실행 방지
    >     ) as dag:
    >         process_task = PythonOperator(
    >             task_id="process_input_value",
    >             python_callable=process_input_value,
    >             provide_context=True,  # context 전달
    >         )
    >     ```
    >     
    > 
    >        `Airflow DAG에서 입력값 처리: dag_run.conf로 전달된 입력값을 수신하고 처리`
    > 
    
    **프론트엔드 (Template)**
    
    > **`📑 Template`**
    > 
    > - [**`index.html`**] `(메인 페이지)`
    >     
    >     ```html
    >     <!DOCTYPE html>
    >     <html lang="en">
    >     <head>
    >         {% load static %}
    >         <meta charset="UTF-8">
    >         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    >         <link rel="stylesheet" type="text/css" href="{% static 'search/css/index.css' %}">
    >         <title>옥탑방 플레이리스트</title>
    >     </head>
    >     <body>
    >         <header>
    >             <h1>옥탑방 플레이리스트</h1>
    >         </header>
    >     
    >         <main>
    >             <!-- 검색창 -->
    >             <form action="{% url 'trigger_dag' %}" method="POST">
    >                 {% csrf_token %}
    >                 <input type="radio" id="youtube" name="platform" value="youtube"> YouTube
    >                 <input type="radio" id="spotify" name="platform" value="spotify"> Spotify
    >                 <input type="text" name="input_value" placeholder="노래 제목 혹은 가수명" required>
    >             </form>
    >     
    >             <!-- 인기 차트 -->
    >             <div class="playlist">
    >                 <h2>{{ current_date }} 인기 차트</h2>
    >                 <div class="scroll-container">
    >                     {% for song in daily_songs %}
    >                         <div class="scroll-item">
    >                             <a href="{{ song.song_url }}" target="_blank">
    >                                 <img src="{{ song.thumbnail }}" alt="{{ song.song_title }}">
    >                                 <p>{{ song.song_title }}</p>
    >                             </a>
    >                         </div>
    >                     {% endfor %}
    >                 </div>
    >             </div>
    >     
    >             <!-- 추천 플레이리스트 -->
    >             <div class="playlist">
    >                 <h2>추천 플레이리스트</h2>
    >                 <div class="scroll-container">
    >                     {% for playlist in daily_playlists %}
    >                         <div class="scroll-item">
    >                             <iframe src="{{ playlist.playlist_url }}" width="300" height="380"></iframe>
    >                         </div>
    >                     {% endfor %}
    >                 </div>
    >             </div>
    >         </main>
    >     
    >         <footer>
    >             <p>@ made by 007</p>
    >         </footer>
    >     </body>
    >     </html>
    >     
    >     ```
    >     
    > 
    >          `노래 검색 / 플랫폼 필터 - 필터에 맞는 검색 결과 제공`
    > 
    >          `오늘의 Youtube/Spotify 인기 차트 및 플레이리스트 제공`
    > 
    > - [**`result.html`**] `(검색 결과 페이지)`
    >     
    >     ```html
    >     <!DOCTYPE html>
    >     <html lang="en">
    >     <head>
    >         {% load static %}
    >         <meta charset="UTF-8">
    >         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    >         <link rel="stylesheet" type="text/css" href="{% static 'search/css/result.css' %}">
    >         <title>옥탑방 플레이리스트</title>
    >     </head>
    >     <body>
    >         <!-- 헤더 -->
    >         <header>
    >             <h1>옥탑방 플레이리스트</h1>
    >         </header>
    >     
    >         <div class="main-container">
    >             <!-- 사이드바 -->
    >             <aside class="sidebar">
    >                 <p class="sidebar-title">MENU</p>
    >                 <button id="youtube-button" class="{% if platform == 'youtube' %}active{% endif %}">YouTube</button>
    >                 <button id="spotify-button" class="{% if platform == 'spotify' %}active{% endif %}">Spotify</button>
    >             </aside>
    >     
    >             <!-- 메인 콘텐츠 -->
    >             <div class="main-content">
    >                 <!-- 검색창 -->
    >                 <form action="{% url 'trigger_dag' %}" method="POST">
    >                     {% csrf_token %}
    >                     <input type="radio" id="youtube" name="platform" value="youtube"> YouTube
    >                     <input type="radio" id="spotify" name="platform" value="spotify"> Spotify
    >                     <input type="text" name="input_value" placeholder="노래 제목 혹은 가수명" required>
    >                 </form>
    >     
    >                 <!-- 검색결과 -->
    >                 <section class="result-container">
    >                     <!-- YouTube 추천 -->
    >                     {% if platform == 'youtube' %}
    >                         <div id="youtube-section">
    >                             <!-- 추천 노래 -->
    >                             <div class="youtube-videos-container">
    >                                 <h2>YouTube 추천 곡</h2>
    >                                 {% for song in search_songs %}
    >                                     <div>{{ song.song_title }}</div>
    >                                 {% endfor %}
    >                             </div>
    >                             <!-- 추천 플레이리스트 -->
    >                             <div class="youtube-playlist-container">
    >                                 <h2>YouTube 추천 플레이리스트</h2>
    >                                 {% for playlist in search_playlists %}
    >                                     <div>{{ playlist.playlist_title }}</div>
    >                                 {% endfor %}
    >                             </div>
    >                         </div>
    >                     {% endif %}
    >     
    >                     <!-- Spotify 추천 -->
    >                     {% if platform == 'spotify' %}
    >                         <div id="spotify-section">
    >                             <!-- 추천 노래 -->
    >                             <div class="spotify-recommend-container">
    >                                 <h2>Spotify 추천 곡</h2>
    >                                 {% for song in search_songs %}
    >                                     <div>{{ song.song_title }}</div>
    >                                 {% endfor %}
    >                             </div>
    >                             <!-- 추천 플레이리스트 -->
    >                             <div class="spotify-playlist-container">
    >                                 <h2>Spotify 추천 플레이리스트</h2>
    >                                 {% for playlist in search_playlists %}
    >                                     <div>{{ playlist.playlist_title }}</div>
    >                                 {% endfor %}
    >                             </div>
    >                         </div>
    >                     {% endif %}
    >                 </section>
    >             </div>
    >         </div>
    >     
    >         <!-- 모달 -->
    >         <div class="modal" id="modal">
    >             <div class="modal-content">
    >                 <h2>노래 재생</h2>
    >                 <iframe id="youtube-player"></iframe>
    >             </div>
    >         </div>
    >     
    >         <!-- Toast 메시지 -->
    >         <div id="toast" class="toast"></div>
    >     
    >         <!-- JavaScript -->
    >         <script src="{% static 'search/js/result.js' %}"></script>
    >     </body>
    >     </html>
    >     ```
    >     
    > 
    >          `노래 재검색 / 플랫폼 필터 - 필터에 맞는 검색 결과 제공`
    > 
    >          `해당 노래의 Youtube/Spotify 추천 곡 및 플레이리스트 제공`
    > 
    >          `Youtube Video에 대한 모달 기능 제공 - 음악 플레이어`
    > 
</aside>

## V. 기대효과 및 한계점

<aside>

### 👍🏽 기대효과

1. **통합 검색으로 시간 절약**
    
    > 기존에는 YouTube와 Spotify에서 원하는 노래를 각각 검색해야 원하는 콘텐츠를 찾을 수 있었음
    > 
    
    > 해당 프로젝트로 **`두 플랫폼의 데이터를 통합적으로 제공`**하여 **`한 번의 검색`**으로 관련된 음악과 플레이리스트 추천
    > 
2. **다양한 추천 콘텐츠 제공**
    
    > **YouTube** : 사용자가 만든 콘텐츠(커버곡, 라이브 영상 등 video)가 풍부
    **Spotify** : 전문적으로 큐레이팅된 플레이리스트를 제공
    > 
    
    > **`두 플랫폼의 특성을 결합`**하여 사용자에게 **`다양한 선택지를 제공`**
    > 
3. **검색과 동시에 재생 가능**
    
    > 각 플랫폼에서 추천 받은 노래를 **`웹페이지에서 바로 재생`**이 가능하도록 Web UI 제공
    > 
4. **검색과 동시에 playlist 추가 가능**
    
    > 각 플랫폼에서 추천 받은 playlist를 **`웹페이지에서 바로 플랫폼의 playlist로 추가`**할 수 있도록 Web UI 제공
    > 

### ☝🏽 한계점 및 개선점

1. **사용자 선호 반영 한계**
    
    > 현재 시스템은 **`검색어 기반의 추천`**으로, 개별 사용자의 선호나 청취 이력과 같은 심화 정보를 반영하기 어려움.
    > 
2. **맞춤형 추천 기능 추가**
    
    > 사용자의 청취 이력, 좋아요 기록, 즐겨찾기 데이터를 저장 및 분석하여 **`개인 맞춤형 추천`** 제공
    > 
3. **추천 사이트 확장**
    
    > spotify, youtube 외에 **`다른 음원 사이트의 추천 리스트 및 추천곡`**을 받아올 수 있도록 api 사용 확장
    > 
</aside>

## VI.  진행과정 및 리뷰

<aside>

### **🔱 Strategy**

- 구현할 기능들을 세 가지로 파트로 분류하여 구현, **`각 기능에 대한 기술을 사용하고 이해`**
- 데이터 **`추출(Extract)`**, **`변환(Transform)`**, **`적재(Load)`** 과정인 ETL/ELT 이해 및 구현
- **`airflow`** 및 **`docker`** 사용법에 대한 이해 및 구현
- **`django`**와 **`airflow`**의 **`connection`** 및 **`dag trigger`** 이해 및 구현


### 💯 기술적 성취도

| Practical solution | ★★★★★ |
| --- | --- |
| Visualization | ★★★★★ |
| Maintainability | ★★★★★ |
| Flexibility | ★★★★☆ |
| Integration | ★★★★★ |
</aside>

</aside>

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
![데이터 아키텍ㅊ](https://github.com/user-attachments/assets/45b04a82-6f4b-4872-8a2e-3bca35d72ac9)

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
    
    ![메인페이지](https://github.com/user-attachments/assets/8b796073-2778-476b-96d8-862318d77e06)

- **`Youtube`**
    
    ![유튜브_페이지](https://github.com/user-attachments/assets/d82df897-dcf7-454d-b3f0-7e18146c4dd0)

    
- **`Spotify`**
    
    ![스포티파이_페이지](https://github.com/user-attachments/assets/85d0f6cb-c1f5-424c-9cad-bf488c1bee70)

    
- **`Play`**

    ![재생페이지](https://github.com/user-attachments/assets/6d3aabd6-2ff9-41f1-afb6-41fcbdb97e08)

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
    > - [**`spotify_today_playlists_dag.py`**] `Spotify의 playlist 중 top 키워드를 포함하는 playlist 중 상위 10개 (매일 자정 갱신)`


    > - [**`songs_dag.py`**] `검색어 기반 Spotify 추천 상위 10개 track / Spotify 추천 목록 10개 기반 Youtube 상위 video (Django input trigger 갱신)`
  
    > - [**`playlist_dag.py`**] `검색어 기반 Spotify 추천 상위 10개 playlist / 검색어 기반 Youtube playlist 중 상위 10개 playlist (Django input trigger 갱신)`
     
    > - [**`spotify_class.py`**] `spotify api 사용을 위한 class`
 
    > - [**`youtube_class.py`**] `youtube api 사용을 위한 class`
  
    
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

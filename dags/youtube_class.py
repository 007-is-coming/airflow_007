import requests
import pandas as pd
from airflow.models import Variable
from spotipy.oauth2 import SpotifyClientCredentials
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import html

# YouTube Data API 설정

class YoutubeClient:
    def __init__(self):
        self.API_KEY = Variable.get("API_KEY") # airflow Var
        self.SEARCH_URL = Variable.get("SEARCH_URL")
        self.BASE_URL = Variable.get("BASE_URL")

    def search_youtube_playlist(self, song_title, max_results=10):
        params = {
            'key': self.API_KEY,
            'q': song_title,
            'type': 'playlist',
            'part': 'snippet',
            'maxResults': max_results
        }
        response = requests.get(self.SEARCH_URL, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            return pd.DataFrame()  # 빈 DataFrame 반환

        data = response.json()
        playlists = []
        for idx, item in enumerate(data.get('items', []), 1):
            title = item['snippet']['title']
            title = html.unescape(title)
            playlist_id = item['id']['playlistId']
            thumbnails = item["snippet"].get("thumbnails", {})
            thumbnail_url = thumbnails.get("medium", {}).get("url", "")  # 썸네일 URL 가져오기
            playlists.append({
                "no": idx,
                "playlist_title": item["snippet"]["title"],
                "playlist_id": playlist_id,
                'playlist_thumbnail': thumbnail_url
            })

        return pd.DataFrame(playlists)
    
    def search_youtube(self, youtube_recommendations_data, max_results=10):
        """
        특정 노래 제목으로 동영상과 플레이리스트를 
        10개씩 검색하여 DataFrame으로 반환하는 함수.
        """
        #spotify 노래 받아오기
        videos = []
        for search_keyword in youtube_recommendations_data:
            #spotify 노래 기준 search
            params = {
                'key': self.API_KEY,
                'q': search_keyword,
                'type': 'video',
                'part': 'snippet',
                'maxResults': 1
            }
            response = requests.get(self.SEARCH_URL, params=params)

            if response.status_code != 200:
                print(f"Error: {response.status_code}, {response.text}")
                return pd.DataFrame()  # 빈 DataFrame 반환
            
            data = response.json()
            
            title = data.get('items')[0]['snippet']['title']
            title = html.unescape(title)
            video_id = data.get('items')[0]['id']['videoId']
            idx = len(videos) + 1
            videos.append({'no': idx, 'video_title': title, 'video_id': video_id})

        return pd.DataFrame(videos)

    def daily_youtube(self):
        # 1. '음악' 카테고리의 인기 비디오 가져오기
        url = f"{self.BASE_URL}/videos"
        params = {
            "part": "snippet,statistics",
            "chart": "mostPopular",
            "videoCategoryId": "10",  # 음악 카테고리
            "maxResults": 10,  # Top 10
            "key": self.API_KEY,
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            videos = data.get("items", [])
            video_list = []

            # 2. 비디오 정보를 정리
            for idx, video in enumerate(videos, 1):
                video_id = video["id"]
                # video_id가 문자열인지 확인
                if isinstance(video_id, str):
                    video_id = video["id"]  # id가 문자열이라면 바로 사용
                elif isinstance(video_id, dict):
                    video_id = video_id.get("videoId", "")  # 딕셔너리에서 videoId 추출
                video_list.append({
                    "no": idx,
                    "video_title": video["snippet"]["title"],
                    "video_id": video_id
                })

        else:
            print(f"API 요청 실패: {response.status_code}, {response.text}")
            return []

        # 1. '음악' 카테고리의 인기 플레이리스트 가져오기
        url = f"{self.BASE_URL}/search"
        params = {
            "part": "snippet",
            "type": "playlist",  # 플레이리스트만 검색
            "maxResults": 10,  # Top 10
            "key": self.API_KEY,
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            playlists = data.get("items", [])
            playlist_list = []

            # 2. 플레이리스트 정보를 정리
            for idx, playlist in enumerate(playlists, 1):
                playlist_id = playlist["id"].get("playlistId", "")
                thumbnails = playlist["snippet"].get("thumbnails", {})
                thumbnail_url = thumbnails.get("medium", {}).get("url", "")  # 썸네일 URL 가져오기

                playlist_list.append({
                    "no": idx,
                    "playlist_title": playlist["snippet"]["title"],
                    "playlist_id": playlist_id,
                    'playlist_thumbnail': thumbnail_url
                })

            return pd.DataFrame(video_list), pd.DataFrame(playlist_list)
        else:
            print(f"API 요청 실패: {response.status_code}, {response.text}")
            return []

import os
import spotipy
from airflow.models import Variable
from spotipy.oauth2 import SpotifyClientCredentials
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
import requests
import base64

class SpotifyClient:
    def __init__(self):
        """ 환경 변수 가져오기 """
        client_id = Variable.get("CLIENT_ID")
        client_secret = Variable.get("CLIENT_SECRET")

        # Spotipy initialization
        self.scope = "playlist-read-private playlist-read-collaborative"
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=client_id,
                client_secret=client_secret,
            )
        )
        
    def get_recommendations(self, song_title):
        """ 추천곡을 가져오는 함수 """
        # 노래 검색
        results = self.sp.search(q=song_title, type='track', limit=1)
        
        if not results['tracks']['items']:
            print("No track found with that name.")
            return []
        
        track = results['tracks']['items'][0]
        print(f"Found track: {track['name']} by {track['artists'][0]['name']}")

        # 추천 곡 받기
        recommendations = self.sp.recommendations(seed_tracks=[track['id']], limit=20)
        
        recommendations_data = []
        youtube_recommendations_data = []
        for rec in recommendations['tracks']:
            album_cover_url = rec['album']['images'][0]['url']
            song_info = {
                "title": rec['name'],
                "link": rec['external_urls']['spotify'],
                "cover_image": album_cover_url
            }
            if len(recommendations_data) < 10:
                recommendations_data.append(song_info)
            else:
                youtube_recommendations_data.append(rec['name'])

        return recommendations_data, youtube_recommendations_data

    def find_playlists_by_song(self, song_title):
        """ 노래 제목을 입력받아 해당 노래가 포함된 플레이리스트를 찾는 함수 """
        # 노래 검색
        results = self.sp.search(q=song_title, type='track', limit=10)
        
        if not results['tracks']['items']:
            print("No track found with that name.")
            return []
        
        track = results['tracks']['items'][0]
        print(f"Found track: {track['name']} by {track['artists'][0]['name']}")

        # 해당 트랙을 포함한 플레이리스트 검색
        playlists = self.sp.search(q=track['name'], type='playlist', limit=10)
        
        if not playlists['playlists']['items']:
            print("No playlists found containing this song.")
            return []
        
        playlist_data = []
        for playlist in playlists['playlists']['items']:
            playlist_name = playlist['name']
            playlist_url = playlist['external_urls']['spotify']
            playlist_cover_url = playlist['images'][0]['url'] if playlist['images'] else 'No image available'
            playlist_info = {
                "title": playlist_name,
                "link": playlist_url,
                "cover_image": playlist_cover_url
            }
            playlist_data.append(playlist_info)
            
        return playlist_data
    
    def get_top_10_playlists(self):
        # 'Top'이라는 키워드로 플레이리스트 검색
        results = self.sp.search(q="Top", type='playlist', limit=10)

        if not results['playlists']['items']:
            print("No playlists found.")
            return

        print(f"Top 10 playlists:")
        today_playlists_data = []
        for idx, playlist in enumerate(results['playlists']['items'], 1):
            playlist_name = playlist['name']
            playlist_url = playlist['external_urls']['spotify']
            playlist_cover_url = playlist['images'][0]['url'] if playlist['images'] else 'No image available'
            playlist_info = {
                "title": playlist_name,
                "link": playlist_url,
                "cover_image": playlist_cover_url
            }
            today_playlists_data.append(playlist_info)
            
        return today_playlists_data
    
    def get_top_10_tracks_from_playlist(self):
        # 'Global Top 50' 플레이리스트 ID
        global_top_50_playlist_id = '37i9dQZEVXbMDoHDwVN2tF'  # 이 ID는 Spotify Global Top 50 플레이리스트의 ID입니다.
        
        # 플레이리스트에서 트랙 가져오기
        results = self.sp.playlist_tracks(global_top_50_playlist_id, limit=10)

        if not results['items']:
            print("No tracks found in the playlist.")
            return

        top_songs = []
        for item in results['items']:
            track = item['track']  # 트랙 정보는 'track' 키 아래에 존재합니다.
            album_cover_url = track['album']['images'][0]['url'] if track['album']['images'] else 'No image available'
            song_info = {
                "title": track['name'],
                "link": track['external_urls']['spotify'],
                "cover_image": album_cover_url
            }
            top_songs.append(song_info)

        return top_songs
import os
import json
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        video_response = self.youtube.videos().list(part='snippet,statistics',
                                                    id=video_id
                                                    ).execute()
        self.video_id = video_id
        self.title: str = video_response['items'][0]['snippet']['title']
        self.views: int = video_response['items'][0]['statistics']['viewCount']
        self.likes: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_info = self.youtube.playlists().list(id=playlist_id,
                                                           part='snippet, contentDetails, status').execute()
        self.playlist_name = self.playlist_info['items'][0]['snippet']['title']
        self.video_response = self.youtube.videos().list(part='snippet,statistics', id=video_id).execute()
        self.video_name = self.video_response['items'][0]['snippet']['title']

    def __str__(self):
        return f'{self.video_name} ({self.playlist_name})'


video1 = Video('9lO06Zxhu88')
video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
print(video1)
print(video2)

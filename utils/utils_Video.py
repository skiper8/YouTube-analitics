import os
import json
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            video_response = self.youtube.videos().list(part='snippet,statistics',
                                                        id=video_id
                                                        ).execute()
            self.title: str = video_response['items'][0]['snippet']['title']
            self.views: int = video_response['items'][0]['statistics']['viewCount']
            self.likes: int = video_response['items'][0]['statistics']['likeCount']

        except Exception:
            self.title = None
            self.views = None
            self.likes = None

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


broken_video = Video('broken_video_id')
print(broken_video.title)
print(broken_video.likes)


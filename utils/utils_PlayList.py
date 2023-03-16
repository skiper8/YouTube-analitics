import os
from googleapiclient.discovery import build
import datetime
import isodate


class PlayList:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.url = 'https://www.youtube.com/playlist?list='+playlist_id
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails',
                                                            maxResults=50).execute()
        self.title = self.playlist['items'][0]['snippet']['title']

    @property
    def total_duration(self):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        response = youtube.videos().list(part='contentDetails,statistics', id=','.join(video_ids)).execute()

        total_duration = datetime.timedelta()

        for video in response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration


    def show_best_video(self):
        likes = []
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        for id in video_ids:
            video_response = youtube.videos().list(part='snippet,statistics',
                                                   id=id
                                                   ).execute()
            like_count: int = int(video_response['items'][0]['statistics']['likeCount'])
            likes.append(like_count)

        for id in video_ids:
            video_response = youtube.videos().list(part='snippet,statistics',
                                                   id=id
                                                   ).execute()
            like_count: int = int(video_response['items'][0]['statistics']['likeCount'])
            if like_count == max(likes):
                print(f'https://youtu.be/{id}')


pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(pl.title)
print(pl.url)
duration = pl.total_duration
print(duration)
print(type(duration))
print(duration.total_seconds())
pl.show_best_video()


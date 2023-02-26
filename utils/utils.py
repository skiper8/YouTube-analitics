import os
import json
from googleapiclient.discovery import build


class Channel:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    info_channel = json.dumps(channel, indent=2, ensure_ascii=False)

    def __init__(self, channel_id):
        self._channel_id = self.channel['items'][0]['id']
        self.title = self.channel['items'][0]['snippet']['title']
        self.channel_description = self.channel['items'][0]['snippet']['description']
        self.channel_url = "https://www.youtube.com/channel/" + channel_id
        self.num_subscribers = self.channel['items'][0]['statistics']['subscriberCount']
        self.num_videos = self.channel['items'][0]['statistics']['videoCount']
        self.num_views = self.channel['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self._channel_id

    def print_info(self):
        print(self.info_channel)
        return json.loads(self.info_channel)

    def get_service(self):
        return self.youtube

    def save_to_json(self, file_path):
        channel_info = {
            "channel_id": self._channel_id,
            "title": self.title,
            "channel_description": self.channel_description,
            "channel_url": self.channel_url,
            "num_subscribers": self.num_subscribers,
            "num_videos": self.num_videos,
            "num_views": self.num_views
        }
        with open(file_path, "w", encoding='UTF-8') as file:
            json.dump(channel_info, file, indent=4)

import os
import json
from googleapiclient.discovery import build


class Channel:

    def __init__(self, channel_id1):
        self.channel_id1 = channel_id1  # вДудь

    def print_info(self):
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('API_KEY')
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id1, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

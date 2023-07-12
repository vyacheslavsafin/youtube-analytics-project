import json

from src.channel import Channel


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        youtube = Channel.get_service()
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=self.video_id
                                               ).execute()
        self.title = video_response["items"][0]["snippet"]["title"]
        self.url = "https://www.youtube.com/watch?v=" + self.video_id
        self.view_count = video_response["items"][0]["statistics"]["viewCount"]
        self.statistic_count = video_response["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

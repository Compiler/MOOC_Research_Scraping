import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow



RowanRobotics_channel_id = "UCy3avhfHpBbbgwZpNvuVklg"
API_KEY = os.environ["YOUTUBE_API_KEY"]

youtube = build('youtube', 'v3', developerKey = API_KEY)





def get_channel_metrics(youtube_instance, channel_id):
    req = youtube_instance.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    res = req.execute()

    print(res)

get_channel_metrics(youtube, RowanRobotics_channel_id)


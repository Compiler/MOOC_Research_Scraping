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




def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()

  print(response)

get_channel_metrics(youtube, RowanRobotics_channel_id)

execute_api_request(
      youtube.reports().query,
      ids='channel==MINE',
      startDate='2017-01-01',
      endDate='2017-12-31',
      metrics='estimatedMinutesWatched,views,likes,subscribersGained',
      dimensions='day',
      sort='day'
  )

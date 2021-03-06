import os, json
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
#API_KEY = os.environ["YOUTUBE_API_KEY"]
CLIENT_SECRETS_FILE = 'client_secret.json'

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

def get_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()

  print(response)

if __name__ == '__main__':
  # Disable OAuthlib's HTTPs verification when running locally.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  start_date = '2017-06-22'
  end_date = '2021-06-29'
  youtubeAnalytics = get_service()
  execute_api_request(
      youtubeAnalytics.reports().query,
      ids='channel==MINE',
      startDate=start_date,
      endDate=end_date,
      metrics='estimatedMinutesWatched,views,likes,subscribersGained',
      dimensions='day',
      sort='day'
  )
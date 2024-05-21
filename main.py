import datetime
import time
import os

import schedule
import tweepy
from dotenv import load_dotenv

from picSearcher import Job

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def createTweet():
    path = Job()
    print("The Path to the Picture is:" + path)

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")

    filename = path

    media_id = api.media_upload(filename=filename).media_id_string
    print(media_id)

    client.create_tweet(media_ids=[media_id])
    print("\n Tweeted for: " + current_time)


schedule.every(1).hours.do(createTweet)

while True:
    schedule.run_pending()
    time.sleep(1)

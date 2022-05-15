import requests
import tweepy
import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    client = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"),
                           consumer_key=os.getenv("CONSUMER_KEY"),
                           consumer_secret=os.getenv("CONSUMER_SECRET"),
                           access_token=os.getenv("ACCESS_TOKEN"),
                           access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))
    response = requests.get("https://kjfacts.herokuapp.com/api/1")

    client.create_tweet(text=response.json()[0])


if __name__ == "__main__":
    main()

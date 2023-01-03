import sys

sys.path.append('../../../')
import tweepy
from ignore_config import (ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN,
                           CONSUMER_KEY, CONSUMER_SECRET)

client = tweepy.Client(
    consumer_key=CONSUMER_KEY, 
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    # bearer_token=BEARER_TOKEN # 
)


def tweet(msg):
    client.create_tweet(text=msg)


def search_recent_tweet(query='Python', max_result=10):
    tweets = client.search_recent_tweets(
        query=query,  # 検索ワード
        max_results=max_result,  # 取得件数
        user_auth=True
        )
    return tweets


if __name__ == '__main__':
    print("finish")

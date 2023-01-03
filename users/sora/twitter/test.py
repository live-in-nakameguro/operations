import sys

sys.path.append('../../../')
import tweepy
from ignore_config import (ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN,
                           CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_ID)

client = tweepy.Client(
    consumer_key=CONSUMER_KEY, 
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    # bearer_token=BEARER_TOKEN
)


def tweet(msg):
    client.create_tweet(text=msg)


def search_recent_tweet(query='Python', max_result=10):
    tweets = client.search_recent_tweets(
        query=query,
        max_results=max_result,
        user_auth=True
        )
    return tweets


def get_users_likes_list(user_id=MY_TWITTER_ID, max_results=5):
    # user_id=468122115 Abe Shinzou (ID checker: https://tweeterid.com/)
    # Docs: https://docs.tweepy.org/en/stable/client.html#tweepy.Client.get_liked_tweets
    parms = {
        'id': user_id, 
        'user_auth': True,
        'max_results': max_results,
        'tweet_fields': [
            'created_at', # tweeted time
        ]
    }
    # liked_tweets = client.get_liked_tweets(id = user_id, user_auth=True)
    liked_tweets = client.get_liked_tweets(**parms)
    return liked_tweets[0]


def get_user_info_with_user_id(user_id=MY_TWITTER_ID):
    # Docs: https://docs.tweepy.org/en/stable/client.html#tweepy.Client.get_user
    parms = {
        'id': user_id, 
        'user_auth': True,
        'user_fields': [
            'id', # user_id
            'name',
            'username', # general user name
            'description', 
            'protected', # bool
        ]
    }
    res = client.get_user(**parms)
    return res[0]


def get_user_info_with_user_name(user_name='AbeShinzo'):
    # Docs: https://docs.tweepy.org/en/stable/client.html#tweepy.Client.get_user
    parms = {
        'username': user_name, 
        'user_auth': True,
        'user_fields': [
            'id', # user_id
            'name',
            'username', # general user ID
            'description', 
            'protected', # bool
        ]
    }
    res = client.get_user(**parms)
    return res[0]


if __name__ == '__main__':
    # from test import get_users_likes
    # get_users_likes_list()
    pass

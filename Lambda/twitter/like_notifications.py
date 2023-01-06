from ignore_config import get_account_key_info

client, MY_TWITTER_ID = get_account_key_info('YabaiSkyYasan')


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


def tweet(msg):
    client.create_tweet(text=msg)


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


def make_tweet_contents(name, username, liked_tweet_list):
    header = f'{name}(@{username}) recently liked below tweets!\n\n'
    # header = f'{name} recently liked below tweets!\n\n'

    body = ''
    for liked_tweet in reversed(liked_tweet_list):
        url = f'●twitter.com/twitter/status/{liked_tweet.id} \n'
        body = body + url

    footer = '\n(tweeted by a python script.)'

    contents = header + body + footer
    
    return contents
    

def execute(user_name):
    user_info = get_user_info_with_user_name(user_name)
    name = user_info.name
    username = user_info.username
    user_id = user_info.id

    liked_tweet_list = get_users_likes_list(user_id=user_id)
    
    # Retrieved last 3 tweets
    liked_tweet_list = liked_tweet_list[:3]
    tweet_contents = make_tweet_contents(name, username, liked_tweet_list)

    print(tweet_contents)
    tweet(tweet_contents)

if __name__=='__main__':
    # execute('kokolifeowataww')
    execute('SkyGonZabuRou')

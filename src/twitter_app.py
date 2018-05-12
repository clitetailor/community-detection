import tweepy

import settings


def create_api():
    app_settings = settings.get_app_settings()
    auth = tweepy.OAuthHandler(
        consumer_key=app_settings['consumer_key'], consumer_secret=app_settings['consumer_secret'])
    auth.set_access_token(
        app_settings['access_token_key'], app_settings['access_token_secret'])
    api = tweepy.API(auth)
    return api

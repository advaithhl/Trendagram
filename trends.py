import logging
import os

import tweepy

# Initialise logging to basic config.
logging.basicConfig()

# Set WOEID to India.
WOEID = 23424848


def get_api():
    try:
        token = os.environ['TRENDAGRAM_TWITTER_BEARER_TOKEN']
        auth = tweepy.OAuth2BearerHandler(token)
        api = tweepy.API(auth)
    except KeyError:
        logging.error(
            'The environment variable for the Twitter Bearer Token was not found. Please make sure that an the Twitter Bearer Token is provided as an environment variable named "TRENDAGRAM_TWITTER_BEARER_TOKEN".')
        exit()
    else:
        return api


def get_trends():
    try:
        api = get_api()
        place_trends = api.get_place_trends(WOEID)
    except tweepy.errors.BadRequest as bad_auth_error:
        logging.error(bad_auth_error)
    except tweepy.errors.TweepyException as tweepy_error:
        logging.error(tweepy_error)
    else:
        return place_trends[0]['trends']

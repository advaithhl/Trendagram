import os

import requests

import trends


def handler(event, context):
    # token = os.getenv('TRENDAGRAM_TELEGRAM_TOKEN')
    # url = f'https://api.telegram.org/bot{token}/getMe'
    # response = requests.get(url)
    # return response.json()

    # Just return all_trends for now.
    all_trends = trends.get_trends()
    return all_trends

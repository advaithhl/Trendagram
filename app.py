import os
import requests

def handler(event, context):
    token = os.getenv('TRENDAGRAM_TELEGRAM_TOKEN')
    url = f'https://api.telegram.org/bot{token}/getMe'
    response = requests.get(url)
    return response.json()

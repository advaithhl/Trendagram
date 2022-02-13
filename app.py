import os

import requests

import trends


def handler(event, context):
    try:
        # Fetch the Telegram bot token.
        TOKEN = os.environ['TRENDAGRAM_TELEGRAM_TOKEN']

        # Fetch the chat ID to send the message to.
        CHAT_ID = os.environ['CHAT_ID']
    except KeyError as ke:
        print(
            f'One or more environment variables were not found. Cannot find a variable named {ke}.')
    else:
        # Get all the trends using the `trends.get_trends` method.
        all_trends = trends.get_trends()

        # Set message to empty.
        trends_message_list = []

        # Create the message
        for idx, trend in enumerate(all_trends, start=1):
            trends_message_list.append(f'{idx}. {trend["name"]}')
        trends_message = '\n'.join(trends_message_list)

        # Make the `sendMessage` request using Telegram API.
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        payload = {
            'chat_id': CHAT_ID,
            'text': trends_message,
            'disable_notification': True,
            'protect_content': True,
        }
        response = requests.post(
            url=url,
            data=payload,
        )

        # Print the response locally (or to CloudWatch logs in production).
        print(response.text)

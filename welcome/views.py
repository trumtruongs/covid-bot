from django.shortcuts import render
import requests
from covidbot import settings


# Create your views here.
def call_send_api(page_id, message_data):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messenger_profile?access_token=%s' % settings.PAGE_ACCESS_TOKEN
    result = requests.post(post_message_url, json=message_data)
    print(result.json())
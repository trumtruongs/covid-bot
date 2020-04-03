import requests
from covidbot import settings


def call_send_api(page_id, message_data, is_delete=False):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messenger_profile?access_token=%s' % settings.PAGE_ACCESS_TOKEN
    if is_delete:
        result = requests.delete(post_message_url, json=message_data)
    else:
        result = requests.post(post_message_url, json=message_data)
    print(result.json())


def set_field(page_id, field, payload):
    message_data = {
        field: payload
    }
    call_send_api(page_id, message_data)


def delete_field(page_id, field):
    message_data = {
        'fields': [field]
    }
    call_send_api(page_id, message_data, True)
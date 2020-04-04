import requests
from covidbot import settings


def send(fbid, page_id, message_data):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % settings.PAGE_ACCESS_TOKEN
    response_msg = {
        "recipient": {
            "id": fbid
        },
        **message_data
    }
    re = requests.post(post_message_url, json=response_msg)
    print('RE', re.json())


def delete(page_id, message_data):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % settings.PAGE_ACCESS_TOKEN
    status = requests.delete(post_message_url, headers={"Content-Type": "application/json"}, data=message_data)
    print(status.json())


def user_profile(fbid):
    user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': settings.PAGE_ACCESS_TOKEN}
    return requests.get(user_details_url, user_details_params).json()
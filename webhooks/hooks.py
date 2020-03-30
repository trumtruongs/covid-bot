import json
import requests
from os import path
from pprint import pprint
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

PAGE_ACCESS_TOKEN = ""
VERIFY_TOKEN = "2318934571"


def call_send_api(fbid, page_id, message_data):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient": {"id": fbid}, "message": message_data})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    pprint(status.json())


def call_delete_api(page_id, message_data):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN
    status = requests.delete(post_message_url, headers={"Content-Type": "application/json"}, data=message_data)
    pprint(status.json())


def get_user_profile(fbid):
    user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
    return requests.get(user_details_url, user_details_params).json()


def send_typing_on(fbid, page_id):
    message_content = {
        'sender_action': 'typing_on'
    }
    call_send_api(fbid, page_id, message_content)


def send_quick_reply(fbid, page_id, text, quick_replies):
    message_content = {
        'text': text,
        'quick_replies': quick_replies
    }
    call_send_api(fbid, page_id, message_content)


def send_generic_message(fbid, page_id, elements):
    message_content = {
        'type': 'template',
        'payload': {
            'template_type': 'generic',
            'elements': elements
        }
    }
    call_send_api(fbid, page_id, message_content)


def send_button_message(fbid, page_id, buttons):
    message_content = {
        'type': 'template',
        'payload': {
            'template_type': 'button',
            'text': 'this is the test text',
            'buttons': buttons
        }
    }
    call_send_api(fbid, page_id, message_content)


def send_text_message(fbid, page_id, text_message):
    message_data = {
        "text": text_message,
        "metadata": "DEVELOPER_DEFINED_METADATA"
    }
    call_send_api(fbid, page_id, message_data)


def send_static_file(fbid, page_id, file_type, file_path):
    server_url = '/static/files'
    message_content = {
        "attachment": {
            "type": file_type,
            "payload": {
                "url": path.join(server_url, file_path)
            }
        }
    }
    call_send_api(fbid, page_id, message_content)


def receive_message(sender_id, page_id, message):
    is_echo = message["is_echo"]
    message_id = message["mid"]
    app_id = message["app_id"]
    metadata = message["metadata"]

    message_text = message["text"]
    message_attachments = message["attachments"]
    quick_reply = message["quick_reply"]
    if is_echo:
        print('Received echo for message %s and app $d with metadata $s', message_id, app_id, metadata)
        return
    elif quick_reply:
        quick_reply_payload = quick_reply["payload"]
        send_text_message(sender_id, page_id, 'Quick reply tapped!')
        return
    elif message_text:
        # TODO handle message text
        return
    elif message_attachments:
        send_text_message(sender_id, page_id, 'Message with attachment received!')


def receive_postback(sender_id, page_id, postback):
    payload = postback['payload']
    message_content = 'Received postback for user %d and page %d with payload %s.' % sender_id, page_id, payload
    print(message_content)
    send_text_message(sender_id, page_id, "Postback called")


class CovidBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            messaging_event = entry["messaging"][0]
            sender_id = messaging_event['sender']['id']
            page_id = messaging_event['recipient']['id']
            message = messaging_event["message"]
            postback = messaging_event['postback']
            send_typing_on(sender_id, page_id)
            if message:
                return receive_message(sender_id, page_id, message)
            elif postback:
                return receive_postback(sender_id, page_id, postback)
            pprint(messaging_event)
        return HttpResponse()
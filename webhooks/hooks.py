import requests
from covidbot import settings
from os import path
from pprint import pprint
from rest_framework.views import APIView
from django.http.response import HttpResponse
from patients.models import Patient


def call_send_api(fbid, page_id, message_data):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % settings.PAGE_ACCESS_TOKEN
    response_msg = {
        "recipient": {
            "id": fbid
        },
        **message_data
    }
    requests.post(post_message_url, json=response_msg)


def call_delete_api(page_id, message_data):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % settings.PAGE_ACCESS_TOKEN
    status = requests.delete(post_message_url, headers={"Content-Type": "application/json"}, data=message_data)
    pprint(status.json())


def get_user_profile(fbid):
    user_details_url = "https://graph.facebook.com/v2.6/%s" % fbid
    user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': settings.PAGE_ACCESS_TOKEN}
    return requests.get(user_details_url, user_details_params).json()


def send_typing_on(fbid, page_id):
    message_content = {
        'sender_action': 'typing_on'
    }
    call_send_api(fbid, page_id, message_content)


def send_typing_off(fbid, page_id):
    message_content = {
        'sender_action': 'typing_off'
    }
    call_send_api(fbid, page_id, message_content)


# quick_replies = [{
#     "content_type": "text",
#     "title": "Action",
#     "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_ACTION"
# }, {
#     "content_type": "text",
#     "title": "Comedy",
#     "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_COMEDY"
# }, {
#     "content_type": "text",
#     "title": "Drama",
#     "payload": "DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_DRAMA"
# }]
# send_quick_reply(sender_id, page_id, 'This is test message!', quick_replies)
def send_quick_reply(fbid, page_id, text, quick_replies):
    message_content = {
        'message': {
            'text': text,
            'quick_replies': quick_replies
        }
    }
    call_send_api(fbid, page_id, message_content)


# elements = [{
#     'title': "rift",
#     'subtitle': "Next-generation virtual reality",
#     'item_url': "https://www.oculus.com/en-us/rift/",
#     'image_url': 'https://images.unsplash.com/photo-1533907650686-70576141c030?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
#     'buttons': [{
#         'type': "web_url",
#         'url': "https://www.oculus.com/en-us/rift/",
#         'title': "Open Web URL"
#     }, {
#         'type': "postback",
#         'title': "Call Postback",
#         'payload': "Payload for first bubble",
#     }],
# }, {
#     'title': "touch",
#     'subtitle': "Your Hands, Now in VR",
#     'item_url': "https://www.oculus.com/en-us/touch/",
#     'image_url': 'https://images.unsplash.com/photo-1533907650686-70576141c030?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
#     'buttons': [{
#         'type': "web_url",
#         'url': "https://www.oculus.com/en-us/touch/",
#         'title': "Open Web URL"
#     }, {
#         'type': "postback",
#         'title': "Call Postback",
#         'payload': "Payload for second bubble",
#     }]
# }]
# send_generic_message(sender_id, page_id, elements)
def send_generic_message(fbid, page_id, elements):
    message_content = {
        'message': {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'generic',
                    'elements': elements
                }
            }
        }
    }
    call_send_api(fbid, page_id, message_content)


# buttons = [{
#     'type': "web_url",
#     'url': "https://www.oculus.com/en-us/rift/",
#     'title': "Open Web URL"
# }, {
#     'type': "postback",
#     'title': "Trigger Postback",
#     'payload': "DEVELOPER_DEFINED_PAYLOAD"
# }, {
#     'type': "phone_number",
#     'title': "Call Phone Number",
#     'payload': "+16505551234"
# }]
# send_button_message(sender_id, page_id, buttons=buttons, text_message='new test message')
def send_button_message(fbid, page_id, buttons, text_message):
    message_content = {
        'message': {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'button',
                    'text': text_message,
                    'buttons': buttons
                }
            }
        }
    }
    call_send_api(fbid, page_id, message_content)


def send_text_message(fbid, page_id, text_message):
    message_data = {
        'message': {
            "text": text_message,
            "metadata": "DEVELOPER_DEFINED_METADATA"
        }
    }
    call_send_api(fbid, page_id, message_data)


def send_static_file(fbid, page_id, file_type, file_path):
    server_url = '/static/files'
    message_content = {
        'message': {
            'attachment': {
                "type": file_type,
                "payload": {
                    "url": path.join(server_url, file_path)
                }
            }
        }
    }
    call_send_api(fbid, page_id, message_content)


def get_patient(fbid, page_id, patient_index):
    try:
        patient_code = str(patient_index).zfill(4)
        info = Patient.objects.get(code=patient_code)
        response_message = 'Bệnh nhân số ' + patient_index + ':'
        if not info.is_healthy:
            if info.gender == 'male':
                response_message += ' Nam,'
            elif info.gender == 'female':
                response_message += ' Nữ,'
            if info.year_of_birth:
                response_message += ' {} tuổi,'.format(2020-info.year_of_birth)
            response_message += ' ' + info.detail
        else:
            response_message += ' đã khỏi bệnh.'
        send_text_message(fbid, page_id, response_message)
    except Patient.DoesNotExist:
        send_text_message(fbid, page_id, "Mã số bệnh nhân không tồn tại!")


def handle_finding(fbid, page_id, message_text):
    signal = message_text[1:3]
    if signal.lower() == 'bn':
        get_patient(fbid, page_id, message_text[4:])


def receive_message(sender_id, page_id, message):
    is_echo = message.get('is_echo')
    message_id = message.get('mid')
    app_id = message.get('app_id')
    metadata = message.get('metadata')

    message_text = message.get('text')
    message_attachments = message.get('attachments')
    quick_reply = message.get('quick_reply')
    if is_echo:
        print('Received echo for message %s and app $d with metadata $s', message_id, app_id, metadata)
        return
    elif quick_reply:
        quick_reply_payload = quick_reply.get('payload')
        send_text_message(sender_id, page_id, 'Quick reply tapped!')
        return
    elif message_text:
        # TODO
        if message_text[0:1] == '@':
            handle_finding(sender_id, page_id, message_text)
        return
    elif message_attachments:
        send_text_message(sender_id, page_id, 'Message with attachment received!')


def receive_postback(sender_id, page_id, postback):
    payload = postback['payload']
    message_content = 'Received postback for user {} and page {} with payload {}.'.format(sender_id, page_id, payload)
    print(message_content)
    send_text_message(sender_id, page_id, "Postback called {}".format(payload))


class CovidBotView(APIView):
    def get(self, request, format=None):
        mode = self.request.GET['hub.mode']
        token = self.request.GET['hub.verify_token']
        challenge = self.request.GET['hub.challenge']
        if mode and token:
            if token == settings.VERIFY_TOKEN and mode == 'subscribe':
                return HttpResponse(challenge)
        return HttpResponse('Error, invalid token')

    def post(self, request, format=None):
        body = request.data.get('entry')
        entry = body[0]
        messaging_event = entry["messaging"][0]
        sender_id = messaging_event['sender']['id']
        page_id = messaging_event['recipient']['id']
        message = messaging_event.get('message')
        postback = messaging_event.get('postback')
        send_typing_on(sender_id, page_id)
        if message:
            receive_message(sender_id, page_id, message)
        elif postback:
            receive_postback(sender_id, page_id, postback)
        send_typing_off(sender_id, page_id)
        return HttpResponse('Ok')

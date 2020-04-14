import pytz
from django.utils import timezone

from covidbot import settings
from subscribers.models import Subscriber
from webhooks import call_api
from os import path


def typing_on(fbid, page_id):
    message_content = {
        'sender_action': 'typing_on'
    }
    call_api.send(fbid, page_id, message_content)


def typing_off(fbid, page_id):
    message_content = {
        'sender_action': 'typing_off'
    }
    call_api.send(fbid, page_id, message_content)


def quick_reply(fbid, page_id, text, quick_replies):
    message_content = {
        'message': {
            'text': text,
            'quick_replies': quick_replies
        }
    }
    call_api.send(fbid, page_id, message_content)


def generic_message(fbid, page_id, elements):
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
    call_api.send(fbid, page_id, message_content)


def button_message(fbid, page_id, buttons, text_message):
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
    call_api.send(fbid, page_id, message_content)


def request_follow_message(fb):
    pass


def text_message(fbid, page_id, text_message):
    message_data = {
        'message': {
            "text": text_message,
            "metadata": "DEVELOPER_DEFINED_METADATA"
        }
    }
    call_api.send(fbid, page_id, message_data)


def static_file(fbid, page_id, file_type, file_path):
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
    call_api.send(fbid, page_id, message_content)


def notify_admin(old, new):
    now = timezone.now().replace(tzinfo=pytz.timezone(settings.TIME_ZONE))
    admins = Subscriber.objects.filter(is_admin=True)
    for admin in admins:
        text_message(admin.recipient_id, admin.page_id, 'VN Có thông tin ca bệnh mới! {}'.format(now.strftime('%H:%M %d/%m/%Y')))
        text_message(admin.recipient_id, admin.page_id, 'Cũ: {}/{}/{}'.format(old['cases'], old['death'], old['recovered']))
        text_message(admin.recipient_id, admin.page_id, 'Mới: {}/{}/{}'.format(new['cases'], new['death'], new['recovered']))

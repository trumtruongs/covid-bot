import pytz
from django.utils import timezone
from subscribers import commons

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


def generic_message(fbid, page_id, elements, one_time_token=None):
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
    call_api.send(fbid, page_id, message_content, one_time_token)


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


def request_follow_message(fbid, page_id):
    message = {
        'message': {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'one_time_notif_req',
                    'title': 'COVID-19 từ Hóng hớt Cô Vy',
                    'payload': 'NOTIFY_ME'
                }
            }
        }
    }
    call_api.send(fbid, page_id, message)


def text_message(fbid, page_id, text_message, one_time_token=None):
    message_data = {
        'message': {
            "text": text_message,
            "metadata": "DEVELOPER_DEFINED_METADATA"
        }
    }
    call_api.send(fbid, page_id, message_data, one_time_token)


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
        token = admin.one_time_token
        text_message(admin.recipient_id, admin.page_id, 'VN Có thông tin ca bệnh mới! {}'.format(now.strftime('%H:%M %d/%m/%Y')), one_time_token=token)
        text_message(admin.recipient_id, admin.page_id, 'Cũ: {}/{}/{}'.format(old['cases'], old['death'], old['recovered']), one_time_token=token)
        text_message(admin.recipient_id, admin.page_id, 'Mới: {}/{}/{}'.format(new['cases'], new['death'], new['recovered']), one_time_token=token)


def subscribe(sender_id, page_id):
    text_message(sender_id, page_id,
                      'Chào bạn, tụi mình là Chatbot cập nhập tin tức về Covid-19. Hãy yên tâm, các bạn luôn an toàn vì đã có tụi mình cập nhật tin tức “Cô Vy” từng phút từng giây! Muốn biết thêm chi tiết thì hãy bấm vào Menu nhé!')
    commons.add_subscriber(sender_id, page_id)
    request_follow_message(sender_id, page_id)

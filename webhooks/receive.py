from webhooks import send, hooks
from subscribers import commons
from webhooks import quick_replies


def receive_message(sender_id, page_id, message):
    is_echo = message.get('is_echo')
    message_id = message.get('mid')
    app_id = message.get('app_id')
    metadata = message.get('metadata')

    message_text = message.get('text')
    message_attachments = message.get('attachments')
    quick_reply = message.get('quick_reply')
    if is_echo:
        print('Received echo for message {} and app {} with metadata {}'.format(message_id, app_id, metadata))
    elif quick_reply:
        quick_reply_payload = quick_reply.get('payload')
        quick_replies.detect_quick_reply(sender_id, page_id, quick_reply_payload)
    elif message_text:
        if message_text[:1] == '@':
            hooks.handle_finding(sender_id, page_id, message_text)
    elif message_attachments:
        send.text_message(sender_id, page_id, 'Message with attachment received!')


def receive_postback(sender_id, page_id, postback):
    payload = postback['payload']
    message_content = 'Received postback for user {} and page {} with payload {}.'.format(sender_id, page_id, payload)
    print(message_content)
    if payload == 'SUBSCRIBE':
        send.text_message(sender_id, page_id,
                          'Chào bạn, tụi mình là Chatbot cập nhập tin tức về Covid-19. Hãy yên tâm, các bạn luôn an toàn vì đã có tụi mình cập nhật tin tức “Cô Vy” từng phút từng giây! Muốn biết thêm chi tiết thì hãy bấm vào Menu nhé!')
        commons.add_subscriber(sender_id, page_id)
    elif payload == 'STATISTICS':
        quick_replies.statistics_replies(sender_id, page_id)
    elif payload == 'HELP_PATIENT':
        commons.help_find_patient(sender_id, page_id)

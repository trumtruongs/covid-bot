from subscribers import models
from webhooks import send


def add_subscriber(recipient_id, page_id):
    models.Subscriber.objects.update_or_create(recipient_id=recipient_id, page_id=page_id)


def help_find_patient(sender_id, page_id):
    send.text_message(sender_id, page_id,
                      'Để xem thông tin bệnh nhân. Hãy gửi tin nhắn với cú pháp: @BN [MÃ BỆNH NHÂN]\nVí dụ: @BN 1')


def update_token_subscriber(recipient_id, page_id, token):
    models.Subscriber.objects.update_or_create(recipient_id=recipient_id, page_id=page_id, defaults={'one_time_token': token})

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from posts import models
from subscribers.models import Subscriber
from webhooks import send
from covidbot import settings


@receiver(pre_save, sender=models.Post)
def post_model_pre_save(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=models.Post)
def post_model_post_save(sender, instance, created, **kwargs):
    subscribers = []
    if instance.pushAdmin:
        subscribers = Subscriber.objects.filter(is_admin=True)
    if instance.publish:
        subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        if instance.type == 'TEXT':
            send.text_message(subscriber.recipient_id, subscriber.page_id, instance.message)
        elif instance.type == 'UPDATE':
            pass
        elif instance.type == 'SHARE':
            send.generic_message(subscriber.recipient_id, subscriber.page_id, elements=[{
                'title': instance.title,
                'image_url': instance.thumbnail,
                'subtitle': instance.sapo,
                'default_action': {
                    'type': 'web_url',
                    'url': instance.link,
                    'messenger_extensions': True
                }
            }])


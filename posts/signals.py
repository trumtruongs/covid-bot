from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from posts import models
from webhooks import hooks
from covidbot import settings


@receiver(pre_save, sender=models.Post)
def post_model_pre_save(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=models.Post)
def post_model_post_save(sender, instance, created, **kwargs):
    if instance.pushAdmin:
        if instance.type == 'TEXT':
            hooks.send_text_message(settings.FB_ADMIN_UID, '', instance.message)

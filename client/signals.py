from django.db.models.signals import post_save
from django.dispatch import receiver
from client import models
from fanpage.views import insert_page_by_client


@receiver(post_save, sender=models.Client)
def client_model_pre_save(sender, instance, **kwargs):
    access_token = instance.access_token
    insert_page_by_client(access_token)

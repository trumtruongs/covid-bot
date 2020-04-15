from django.db.models.signals import post_save
from django.dispatch import receiver
from posts import models
from webhooks.send import broadcast_in_signals
import _thread


@receiver(post_save, sender=models.Post)
def post_model_post_save(sender, instance, created, **kwargs):
    _thread.start_new_thread(broadcast_in_signals, (instance,))


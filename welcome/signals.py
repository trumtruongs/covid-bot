from django.db.models.signals import post_save
from django.dispatch import receiver
from welcome import models, views


@receiver(post_save, sender=models.Welcome)
def welcome_model_post_save(sender, instance, **kwargs):
    page_id = instance.page_id
    welcome_configs = sender.objects.filter(page_id=page_id,)
    filtered_data = []
    for i in welcome_configs:
        filtered_data.append({
            'locale': i.locale,
            'text': i.text,
        })
    response_message = {
        'greeting': filtered_data,
    }
    views.call_send_api(page_id, response_message)

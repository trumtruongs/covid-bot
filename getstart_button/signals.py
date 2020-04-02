from django.db.models.signals import post_save
from django.dispatch import receiver
from getstart_button import models
from welcome import views


@receiver(post_save, sender=models.GetStartedButton)
def getstart_button_model_post_save(sender, instance, **kwargs):
    page_id = instance.page_id
    welcome_configs = sender.objects.get(page_id=page_id,)
    print(welcome_configs.payload)
    response_message = {
        'get_started': {
            'payload': welcome_configs.payload
        },
    }
    views.call_send_api(page_id, response_message)

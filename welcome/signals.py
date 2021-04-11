from django.db.models.signals import post_save
from django.dispatch import receiver
from welcome import models, views


@receiver(post_save, sender=models.GreetingMessage)
def welcome_model_post_save(sender, instance, **kwargs):
    welcome_configs = sender.objects.filter(fanpage=instance.fanpage,)
    filtered_data = []
    for i in welcome_configs:
        filtered_data.append({
            'locale': i.locale,
            'text': i.text,
        })
    response_message = {
        'greeting': filtered_data,
    }
    views.call_send_api(
        instance.fanpage.id,
        response_message
    )


@receiver(post_save, sender=models.GetStartedButton)
def getstart_button_model_post_save(sender, instance, **kwargs):
    welcome_configs = sender.objects.get(fanpage=instance.fanpage,)
    views.set_field(
        instance.fanpage.id,
        'get_started',
        {
            'payload': welcome_configs.payload
        }
    )


@receiver(post_save, sender=models.PersistentMenu)
def persistent_menu_model_post_save(sender, instance, **kwargs):
    persistent_menu_configs = sender.objects.filter(fanpage=instance.fanpage, )
    payload = []
    for config in persistent_menu_configs:
        payload.append({
            'locale': config.locale,
            'composer_input_disabled': False,
            'call_to_actions': config.call_to_actions
        })
    views.set_field(
        instance.fanpage.id,
        'persistent_menu',
        payload=payload
    )

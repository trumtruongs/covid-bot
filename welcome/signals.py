from django.db.models.signals import post_save
from django.dispatch import receiver
from welcome import models, views


@receiver(post_save, sender=models.GreetingMessage)
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


@receiver(post_save, sender=models.GetStartedButton)
def getstart_button_model_post_save(sender, instance, **kwargs):
    page_id = instance.page_id
    welcome_configs = sender.objects.get(page_id=page_id,)
    print(welcome_configs.payload)
    views.set_field(
        page_id,
        'get_started',
        welcome_configs.payload
    )


@receiver(post_save, sender=models.PersistentMenu)
def persistent_menu_model_post_save(sender, instance, **kwargs):
    page_id = instance.page_id
    persistent_menu_configs = sender.objects.filter(page_id=page_id, )
    payload = []
    for config in persistent_menu_configs:
        payload.append({
            'locale': config.locale,
            'composer_input_disabled': False,
            'call_to_actions': config.call_to_actions
        })
    views.set_field(
        page_id,
        'persistent_menu',
        payload=payload
    )

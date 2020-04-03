from django.db.models.signals import post_save
from django.dispatch import receiver
from persistent_menu import models
from welcome import views


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

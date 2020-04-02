from django.apps import AppConfig


class GetstartButtonConfig(AppConfig):
    name = 'getstart_button'

    def ready(self):
        from getstart_button import signals
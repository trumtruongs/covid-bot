from django.apps import AppConfig


class WelcomeConfig(AppConfig):
    name = 'welcome'

    def ready(self):
        from welcome import signals
from django.apps import AppConfig


class PersistentMenuConfig(AppConfig):
    name = 'persistent_menu'

    def ready(self):
        from persistent_menu import signals
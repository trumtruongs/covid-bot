from django.contrib import admin

# Register your models here.
from welcome.models import GreetingMessage, GetStartedButton, PersistentMenu


@admin.register(GreetingMessage)
class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('fanpage', 'locale', 'text',)
    save_on_top = True


@admin.register(GetStartedButton)
class GetStartedButtonAdmin(admin.ModelAdmin):
    list_display = ('fanpage', 'payload')
    save_on_top = True


@admin.register(PersistentMenu)
class PersistentMenuAdmin(admin.ModelAdmin):
    list_display = ('fanpage', 'locale', 'call_to_actions')
    save_on_top = True

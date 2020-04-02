from django.contrib import admin

# Register your models here.
from welcome.models import Welcome


@admin.register(Welcome)
class WelcomeAdmin(admin.ModelAdmin):
    list_display = ('page_id', 'locale', 'text',)
    save_on_top = True
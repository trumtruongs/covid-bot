from django.contrib import admin
from getstart_button.models import GetStartedButton


@admin.register(GetStartedButton)
class GetStartedButtonAdmin(admin.ModelAdmin):
    list_display = ('page_id', 'payload')
    save_on_top = True

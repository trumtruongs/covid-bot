from django.contrib import admin

from subscribers.models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'recipient_id', 'uid', 'page_id', 'created_at', 'updated_at')
    save_on_top = True

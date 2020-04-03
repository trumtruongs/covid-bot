from django.contrib import admin
from persistent_menu.models import PersistentMenu


@admin.register(PersistentMenu)
class PersistentMenuAdmin(admin.ModelAdmin):
    list_display = ('page_id', 'locale', 'call_to_actions')
    save_on_top = True

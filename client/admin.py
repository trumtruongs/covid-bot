from django.contrib import admin
from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'expiresIn')
    raw_id_fields = ('pages',)

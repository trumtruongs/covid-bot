from django.contrib import admin
from fanpage.models import Fanpage


@admin.register(Fanpage)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

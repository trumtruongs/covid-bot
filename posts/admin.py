from django.contrib import admin

# Register your models here.
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'type', 'title', 'created_at', 'updated_at')
    save_on_top = True
    search_fields = ('type', 'title')
    list_filter = ('type',)

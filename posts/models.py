from django.db import models
from django.utils.translation import gettext_lazy as _

POST_TYPES = (
    ('TEXT', 'Nội dung'),
    ('SHARE', 'Chia sẻ Thông tin'),
)


class Post(models.Model):
    message = models.TextField(_('Message'), blank=True)
    thumbnail = models.CharField(_('Link thumbnail'), max_length=500, blank=True)
    title = models.CharField(_('Post Title'), max_length=255, blank=True)
    sapo = models.CharField(_('Post sapo'), max_length=500, blank=True)
    link = models.CharField(_('Link'), max_length=500, blank=True)
    type = models.CharField(_('Post type messenger'), choices=POST_TYPES, max_length=20, default='TEXT')
    pushAdmin = models.BooleanField(_('Push Admin'), default=False, help_text=_('Push message to admin'))
    publish = models.BooleanField(_('Publish'), default=False, help_text=_('Broadcast message'))

    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscriber(models.Model):
    display_name = models.CharField(_('Display name'), max_length=255, blank=True)
    recipient_id = models.CharField(_('Recipient ID'), max_length=50, db_index=True)
    one_time_token = models.CharField(_('One time TOKEN'), max_length=255, db_index=True, blank=True)
    message_id = models.CharField(_('Message ID'), max_length=255, db_index=True, blank=True)
    page_id = models.CharField(_('Page ID'), max_length=50, db_index=True)
    uid = models.CharField(_('Facebook UID'), max_length=50, db_index=True, blank=True)
    is_admin = models.BooleanField(_('Is Admin'), default=False, db_index=True)

    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.display_name, self.recipient_id)
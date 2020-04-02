from django.db import models
from django.utils.translation import gettext_lazy as _

LOCALES = (
    ('default', 'Default'),
    ('en_US', 'US'),
    ('vi_VN', 'Vietnam'),
)


class Welcome(models.Model):
    locale = models.CharField(_('Locale'), max_length=50, choices=LOCALES, db_index=True)
    text = models.CharField(_('Welcome message'), max_length=160)
    page_id = models.CharField(_('Page ID'), max_length=20, db_index=True)

    class Meta:
        unique_together = (('locale', 'page_id'),)

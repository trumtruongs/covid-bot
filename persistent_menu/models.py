from django.db import models
from django.utils.translation import gettext_lazy as _

LOCALES = (
    ('default', 'Default'),
    ('en_US', 'US'),
    ('vi_VN', 'Vietnam'),
)


# Create your models here.
class PersistentMenu(models.Model):
    call_to_actions = models.TextField(
        _('Call to Actions payload'),
        max_length=1024,
        help_text="Please use the following format:"
                  "</br>[{"
                  "</br>&nbsp;&nbsp;'title': 'Talk to an agent',"
                  "</br>&nbsp;&nbsp;'type': 'postback',"
                  "</br>&nbsp;&nbsp;'payload': 'CARE_HELP',"
                  "</br>},"
                  "</br>{"
                  "</br>&nbsp;&nbsp;'title': 'Outfit suggestions',"
                  "</br>&nbsp;&nbsp;'type': 'postback',"
                  "</br>&nbsp;&nbsp;'payload': 'CURATION',"
                  "</br>},"
                  "</br>{"
                  "</br>&nbsp;&nbsp;'title': 'Shop now',"
                  "</br>&nbsp;&nbsp;'type': 'web_url',"
                  "</br>&nbsp;&nbsp;'url': 'https://www.facebook.com/vihu96',"
                  "</br>&nbsp;&nbsp;'webview_height_ratio': 'full',"
                  "</br>}]"
    )
    locale = models.CharField(_('Locale'), max_length=50, choices=LOCALES, db_index=True, default='default')
    page_id = models.CharField(_('Page ID'), max_length=20, db_index=True, unique=True)

    class Meta:
        unique_together = (('locale', 'page_id'),)

from django.db import models
from django.utils.translation import gettext_lazy as _
from fanpage.models import Fanpage

LOCALES = (
    ('default', 'Default'),
    ('en_US', 'US'),
    ('vi_VN', 'Vietnam'),
)


class GreetingMessage(models.Model):
    locale = models.CharField(_('Locale'), max_length=50, choices=LOCALES, db_index=True)
    text = models.CharField(_('Greeting message'), max_length=160)
    fanpage = models.ForeignKey(to=Fanpage, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.fanpage.name

    class Meta:
        unique_together = (('locale', 'fanpage'),)


class GetStartedButton(models.Model):
    payload = models.CharField(_('Get Started Payload'), max_length=512)
    fanpage = models.ForeignKey(to=Fanpage, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.fanpage.name


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
    fanpage = models.ForeignKey(to=Fanpage, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.fanpage.name

    class Meta:
        unique_together = (('locale', 'fanpage'),)

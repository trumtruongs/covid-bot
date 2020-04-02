from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class GetStartedButton(models.Model):
    payload = models.CharField(_('Get Started Payload'), max_length=512)
    page_id = models.CharField(_('Page ID'), max_length=20, db_index=True, unique=True)

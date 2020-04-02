from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Fanpage(models.Model):
    id = models.CharField(_('Page ID'), primary_key=True, max_length=50, blank=False)
    name = models.CharField(_('Page Name'), max_length=255, blank=False, db_index=True)
    access_token = models.CharField(_('Access Token'), max_length=255, blank=False)
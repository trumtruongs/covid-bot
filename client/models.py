from django.db import models
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    user_id = models.CharField(_('User ID'), max_length=20, blank=False, primary_key=True)
    email = models.EmailField(_('Email'), max_length=50)
    access_token = models.CharField(_('Access Token'), max_length=255, blank=False)
    expiresIn = models.DateTimeField(_('Expires In'))
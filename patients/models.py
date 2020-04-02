from django.db import models
from django.utils.translation import gettext_lazy as _


GENDERS = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('', 'Not defined'),
)


class Patient(models.Model):
    code = models.CharField(_('Patient Code'), max_length=10, blank=False, unique=True)
    is_healthy = models.BooleanField(_('Patient is healthy?'), default=False)
    gender = models.CharField(_('Gender'), choices=GENDERS, max_length=20, default='', blank=True)
    year_of_birth = models.PositiveIntegerField(_('Year of birth'), max_length=4, blank=True)
    address = models.CharField(_('Address'), max_length=255, db_index=True, blank=True)
    detail = models.TextField(_('Detail'), blank=True)

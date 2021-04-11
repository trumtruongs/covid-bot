from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    code = models.CharField(_('Country Code'), max_length=2, db_index=True, unique=True)
    name = models.CharField(_('Country Name'), max_length=255)
    cases = models.IntegerField(_('Total cases'), default=0)
    death = models.IntegerField(_('Total death'), default=0)
    recovered = models.IntegerField(_('Total recovered'), default=0)
    description = models.TextField(_('Description'), default='', blank=True)

    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class History(models.Model):
    country = models.ForeignKey(Country, related_name='+', on_delete=models.CASCADE)
    date = models.DateField(_('Date'), auto_now_add=True, db_index=True)

    cases = models.IntegerField(_('Cases'), default=0)
    death = models.IntegerField(_('Death'), default=0)
    recovered = models.IntegerField(_('Recovered'), default=0)
    description = models.TextField(_('Description'), default='', blank=True)

    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country.name

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'
        unique_together = (('country', 'date'),)

from django.contrib import admin
from countries.models import History, Country


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'date', 'cases', 'death', 'recovered', 'created_at', 'updated_at')
    raw_id_fields = ('country',)
    save_on_top = True

    def country_name(self, obj):
        return obj.country.name


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'cases', 'death', 'recovered', 'created_at', 'updated_at')
    save_on_top = True


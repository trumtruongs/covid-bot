from django.contrib import admin
from patients.models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_healthy', 'gender', 'year_of_birth', 'address', 'detail')
    list_filter = ('is_healthy', 'gender')
    search_fields = ('code',)
    actions = ('is_healthy', 'is_not_healthy',)

    def is_healthy(self, request, qs):
        qs.update(is_healthy=True)

    def is_not_healthy(self, request, qs):
        qs.update(is_healthy=True)

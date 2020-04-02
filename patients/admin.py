from django.contrib import admin
from patients.models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_healthy', 'gender', 'year_of_birth', 'address', 'detail')

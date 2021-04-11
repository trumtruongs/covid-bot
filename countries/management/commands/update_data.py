from django.core.management.base import BaseCommand, CommandError
from countries.commons import fetch_new_statistics


class Command(BaseCommand):
    help = 'Update ca nhiễm mới nè!!'

    def handle(self, *args, **options):
        fetch_new_statistics()

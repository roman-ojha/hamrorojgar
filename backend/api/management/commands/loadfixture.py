from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('loaduser')
        call_command('loaddata', 'fixtures/address.json')
        call_command('loaddata', 'fixtures/citizen.json')
        call_command('loaddata', 'fixtures/government.json')
        call_command('loaddata', 'fixtures/vacancy.json')
        call_command('loaddata', 'fixtures/qualification.json')
        call_command('loaddata', 'fixtures/job_application.json')

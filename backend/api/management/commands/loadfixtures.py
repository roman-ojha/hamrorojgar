from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import Permission, Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('loaduser')
        call_command('loaddata', 'fixtures/address.json')
        call_command('loaddata', 'fixtures/citizen.json')
        call_command('loaddata', 'fixtures/government.json')
        call_command('loaddata', 'fixtures/vacancy.json')
        call_command('loaddata', 'fixtures/qualification.json')
        call_command('loaddata', 'fixtures/job_application.json')
        call_command('loaddata', 'fixtures/mainDBCitizen.json')
        call_command('loaddata', 'fixtures/payment_gateway.json')
        call_command('loaddata', 'fixtures/district.json')
        call_command('loaddata', 'fixtures/municipality.json')

        permissions = [
            'view_address',
            'view_user',
            'view_citizenuser',
            'view_citizen',
            'view_governmentuser',
            'view_government',
            'add_vacancy',
            'change_vacancy',
            'delete_vacancy',
            'view_vacancy',
            'add_qualification',
            'change_qualification',
            'delete_qualification',
            'view_qualification',
            'add_jobapplication',
            'change_jobapplication',
            'view_jobapplication',
            'view_district',
            'view_municipality',
            'view_citizen',
        ]
        # Create a new group and assign permissions to it
        group_name = 'government'  # Change this to the desired group name
        group, created = Group.objects.get_or_create(name=group_name)

        # Add permissions to the group
        for codename in permissions:
            pms = Permission.objects.filter(codename=codename)
            for permission in pms:
                group.permissions.add(permission)

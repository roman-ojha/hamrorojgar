from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.core.management import call_command
from api.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        fixture_path = 'fixtures/users.json'

        # Load the fixture data
        call_command('loaddata', fixture_path)

        # Retrieve the User objects from the fixture data
        users = User.objects.all()

        # Hash the passwords for each User
        for user in users:
            # Retrieve the plaintext password from the fixture data
            plaintext_password = user.password

            # Hash the password
            hashed_password = make_password(plaintext_password)

            # Update the User object with the hashed password
            user.password = hashed_password
            user.save()

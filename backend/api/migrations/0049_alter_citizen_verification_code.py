# This is the custom migration
from django.db import migrations, models
from utils.generate_unique_hash import generate_unique_hash


def set_my_defaults(apps, schema_editor):
    from api.models import citizen
    citizens = citizen.Citizen.objects.filter(verification_code=None)
    for citizen in citizens:
        citizen.verification_code = generate_unique_hash()
        citizen.save()


def reverse_func(apps, schema_editor):
    pass  # code for reverting migration, if any


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_citizen_is_valid_number_citizen_verification_code'),
    ]

    operations = [
        migrations.RunPython(set_my_defaults, reverse_func),
        migrations.AlterField(
            model_name='citizen',
            name='verification_code',
            field=models.TextField(),
        ),
    ]

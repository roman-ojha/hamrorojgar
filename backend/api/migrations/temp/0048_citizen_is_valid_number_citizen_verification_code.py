# Generated by Django 4.2.1 on 2023-06-24 10:32
from django.db import migrations, models
from utils.generate_unique_hash import generate_unique_hash


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_vacancy_job_location_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='is_valid_number',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='citizen',
            name='verification_code',
            field=models.TextField(null=True),
        ),
    ]

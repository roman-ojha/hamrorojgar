# Generated by Django 4.2.1 on 2023-05-15 09:53

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_citizen'),
    ]

    operations = [
        migrations.CreateModel(
            name='GovernmentUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.user',),
            managers=[
                ('government', django.db.models.manager.Manager()),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_remove_vacancy_opened_by_vacancy_government_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='photo_url',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-18 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_jobapplication_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='citizen',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='api.citizen'),
            preserve_default=False,
        ),
    ]
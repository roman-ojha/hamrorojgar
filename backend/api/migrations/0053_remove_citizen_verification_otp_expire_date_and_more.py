# Generated by Django 4.2.1 on 2023-06-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_citizen_verification_otp_expire_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='verification_otp_expire_date',
        ),
        migrations.AddField(
            model_name='citizen',
            name='d7_otp_id',
            field=models.TextField(null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-09 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_jobapplication_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='by',
        ),
        migrations.AlterField(
            model_name='payment',
            name='for_application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jobapplication'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_using',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paymentgateway'),
        ),
        migrations.AddField(
            model_name='payment',
            name='by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
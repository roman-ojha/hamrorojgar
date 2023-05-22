# Generated by Django 4.2.1 on 2023-05-22 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_address_remove_citizen_p_address_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='p_address',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='p_address', to='api.address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='citizen',
            name='t_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='t_address', to='api.address'),
        ),
    ]

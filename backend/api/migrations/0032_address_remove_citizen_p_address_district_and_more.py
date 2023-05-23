# Generated by Django 4.2.1 on 2023-05-22 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_citizen_p_address_district_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=200)),
                ('municipality', models.CharField(max_length=100)),
                ('ward_no', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='p_address_district',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='p_address_municipality',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='p_address_ward_no',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='t_address_district',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='t_address_municipality',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='t_address_ward_no',
        ),
    ]
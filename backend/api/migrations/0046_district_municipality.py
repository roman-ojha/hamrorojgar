# Generated by Django 4.2.1 on 2023-06-11 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_remove_payment_by_payment_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('type', models.CharField(choices=[('MAHAHAGAR', 'Mahanagar Palika'), ('UPAMAHANAGAR', 'Upamahanagar Palika'), ('NAGARPALIKA', 'Nagar Palika'), ('GHAUPALIKA', 'Ghau Palika')], max_length=20)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='of_district', to='api.district')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-25 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Futbol', 'Futbol'), ('Golf', 'Golf')], max_length=11, null=True, verbose_name='Randevu tipi')),
                ('day', models.CharField(default='0', max_length=5, verbose_name='Randevu günü')),
                ('month', models.CharField(default='0', max_length=5, verbose_name='Randevu ayı')),
                ('hour', models.CharField(default='0', max_length=5, verbose_name='Randevu saati')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('appointment_owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Randevu sahibi')),
            ],
        ),
    ]

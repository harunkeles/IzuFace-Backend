# Generated by Django 4.0 on 2022-02-14 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussionsmodel',
            name='topic',
        ),
    ]

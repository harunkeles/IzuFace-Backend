# Generated by Django 2.1.15 on 2021-12-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211229_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]

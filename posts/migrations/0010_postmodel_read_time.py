# Generated by Django 4.0 on 2022-02-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_postmodel_modified_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='read_time',
            field=models.CharField(default='0', max_length=5, verbose_name='Gönderi Okuma Süresi'),
        ),
    ]

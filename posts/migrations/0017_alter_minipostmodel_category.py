# Generated by Django 4.0.4 on 2022-06-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_minipostmodel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minipostmodel',
            name='category',
            field=models.CharField(blank=True, help_text='Mini post kategori', max_length=2, null=True, verbose_name='Mini post kategori'),
        ),
    ]

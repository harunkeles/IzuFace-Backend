# Generated by Django 4.0 on 2022-03-01 21:51

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_postmodel_modified_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='user_rank',
            field=models.CharField(blank=sqlalchemy.sql.expression.false, default=0, max_length=999, verbose_name='Kullanıcı rütbesi'),
        ),
    ]

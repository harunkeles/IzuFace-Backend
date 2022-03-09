# Generated by Django 2.1.15 on 2021-12-30 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentUsers', '0009_auto_20211229_0135'),
        ('posts', '0004_tagmodel_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to='studentUsers.StudentUserProfileModel', verbose_name='Postu beğenenler'),
        ),
    ]

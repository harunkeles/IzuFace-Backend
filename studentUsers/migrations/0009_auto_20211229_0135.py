# Generated by Django 2.1.15 on 2021-12-28 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentUsers', '0008_auto_20211229_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuserprofilemodel',
            name='backImage',
            field=models.ImageField(blank=True, default='static/bg.png', null=True, upload_to='studentUsers/background-image', verbose_name='Arka plan fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='studentuserprofilemodel',
            name='profImage',
            field=models.ImageField(blank=True, default='static/user-team.png', null=True, upload_to='studentUsers/profile-image', verbose_name='Profil fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='studentuserprofilemodel',
            name='smallDesc',
            field=models.TextField(blank=True, default='İstanbul Sabahattin Zaim Üniversitesi öğrencisiyim.', max_length=500, null=True, verbose_name='Kişinin kısa açıklaması'),
        ),
    ]
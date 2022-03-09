# Generated by Django 2.1.15 on 2021-12-28 21:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('studentUsers', '0007_auto_20211226_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentexperiencesmodel',
            name='experienceInfo',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(0, 'İş Deneyimi'), (1, 'Staj Deneyimi')], max_length=3, verbose_name='Deneyimi'),
        ),
        migrations.AlterField(
            model_name='studentuserprofilemodel',
            name='profImage',
            field=models.ImageField(blank=True, default='static/user.png', null=True, upload_to='studentUsers/profile-image', verbose_name='Profil fotoğrafı'),
        ),
    ]

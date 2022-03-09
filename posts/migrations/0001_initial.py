# Generated by Django 2.1.15 on 2021-12-25 12:15

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Ana kategori adı')),
                ('slug', models.SlugField(default='emptySlug')),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Post Adı')),
                ('subTitle', models.CharField(blank=True, help_text='Postun alt başlığını giriniz.', max_length=200, null=True, verbose_name='Post alt başlığı')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(help_text='Postun yazısını giriniz.', verbose_name='Post Yazısı')),
                ('image', models.ImageField(blank=True, default='static_img/empty-post-img.png', help_text='Postun resmini seçiniz.', null=True, upload_to='blog/post/', verbose_name='Post Fotoğrafı ')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Post oluşturulma tarihi')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Post güncelleme tarihi')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('post_owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Post sahibi')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Alt kategori adı')),
                ('slug', models.SlugField(default='emptySlug')),
                ('mainCategoryName', models.ForeignKey(default=1, help_text='Alt kategorinin bağlı olduğu ana kategori adı.', on_delete=django.db.models.deletion.CASCADE, related_name='mainCategory_in_subCategory', to='posts.MainCategoryModel', verbose_name='Bağlı olduğu ana kategori adı')),
            ],
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Etiket adı')),
                ('slug', models.SlugField(default='emptySlug')),
            ],
        ),
        migrations.AddField(
            model_name='postmodel',
            name='subCategory',
            field=models.ForeignKey(default=1, help_text="Post'un kategorisini seçiniz.", on_delete=django.db.models.deletion.CASCADE, related_name='subCategory_in_post', to='posts.SubCategoryModel', verbose_name='Alt Kategori'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='Postun etiketlerini seçiniz.', related_name='postsTag', to='posts.TagModel', verbose_name='Post Etiketleri '),
        ),
    ]
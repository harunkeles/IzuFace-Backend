from django.db.models.query import InstanceCheckMeta
from izu_face_manager.settings import TIME_ZONE
from datetime import datetime
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import default, slugify, title
from PIL import Image
from django.db.models.signals import post_save
import datetime
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from colorfield.fields import ColorField
# Create your models here.


class NewsSubCategoryModel(models.Model):
    title = models.CharField(max_length=50, blank=False,verbose_name="Haber alt kategori adı")
    slug = models.SlugField(default="emptySlug", editable=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsSubCategoryModel, self).save(*args, **kwargs)


class NewsTagModel(models.Model):
    title = models.CharField(max_length=30, blank=False, verbose_name="Haber etiket adı")
    color = ColorField(default='#FF0000')
    slug = models.SlugField(default="emptySlug", editable=True)

    def __str__(self):
        return '#'+self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsTagModel, self).save(*args, **kwargs)



class NewsPostModel(models.Model):
    post_owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE, default=1,verbose_name="Haber sahibi")
    subCategory = models.ForeignKey(NewsSubCategoryModel, on_delete=models.CASCADE,default=1, related_name="newsSubCategory_in_post", verbose_name='Haber alt kategori', help_text="Haberin kategorisini seçiniz.")
    title = models.CharField(max_length=300,blank=False,verbose_name='Haberin Adı')
    subTitle = models.CharField(max_length=500, blank=True,null=True,verbose_name="Haberin alt başlığı", help_text='Haberin alt başlığını giriniz.')
    text = RichTextUploadingField(blank=False,verbose_name="Haberin Yazısı", help_text='Haberin yazısını giriniz.',config_name='awesome_ckeditor')
    tag = models.ManyToManyField(NewsTagModel, blank=True, related_name="newsPostsTag",verbose_name='Haber Etiketleri', help_text='Haberin etiketlerini seçiniz.')
    image = models.ImageField(blank=True, null=True, default='static_img/empty-post-img.png',upload_to='users/moderators/'+settings.AUTH_USER_MODEL+'/newsPost', verbose_name="Haberin Fotoğrafı ", help_text='Haberin resmini seçiniz.')
    created_date = models.DateTimeField(editable=True,auto_now_add=False,default=datetime.now,blank=False, null=False, verbose_name="Haberin oluşturulma tarihi")
    modified_date = models.DateTimeField(editable=True,auto_now_add=False,auto_now=True, blank=False, null=False, verbose_name="Haberin güncelleme tarihi")
    slug = models.SlugField(max_length=200,unique=True,editable=True,blank=True,null=True)

    def __str__(self):
        return self.post_owner.username+ ' : "' + self.title + '"'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
        self.slug = slugify(self.title)
        super(NewsPostModel, self).save(*args, **kwargs)
        self.slug = slugify(self.title+"-"+str(self.id))

        image = Image.open(self.image.path)        
        if image.height < 350 or image.width < 650 :
            new_size = (650,350)
            image.thumbnail(new_size)
            image.save(self.image.path)

        return super(NewsPostModel, self).save(*args, **kwargs)

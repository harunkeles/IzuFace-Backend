from statistics import mode
import uuid

from sqlalchemy import false, null
from izu_face_manager.settings import TIME_ZONE
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import default, slugify, title
from PIL import Image
from django.db.models.signals import post_save
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from colorfield.fields import ColorField
from studentUsers.models import StudentUserProfileModel
from django.utils.html import mark_safe

def replaceSlugMethod(slug):
    return slug.replace('ı','i')

class MainCategoryModel(models.Model):
    title = models.CharField(max_length=50, blank=False, verbose_name="Ana kategori adı")
    slug = models.SlugField(default="emptySlug", editable=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MainCategoryModel, self).save(*args, **kwargs)

    # def post_filter(self):
    #     Category.objects.filter(id=SubCategory.category_id).order_by('-id')

class SubCategoryModel(models.Model):
    mainCategoryName = models.ForeignKey(MainCategoryModel, on_delete=models.CASCADE,default=1, related_name="mainCategory_in_subCategory", verbose_name='Bağlı olduğu ana kategori adı', help_text="Alt kategorinin bağlı olduğu ana kategori adı.")
    title = models.CharField(max_length=50, blank=False,verbose_name="Alt kategori adı")
    slug = models.SlugField(default="emptySlug", editable=True)

    def __str__(self):
        return self.mainCategoryName.title+" >> "+self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubCategoryModel, self).save(*args, **kwargs)

    def mainCategoryNames(self):
        return self.mainCategoryName.title


class TagModel(models.Model):
    title = models.CharField(max_length=30, blank=False, verbose_name="Etiket adı")
    color = ColorField(default='#FF0000')
    slug = models.SlugField(default="emptySlug", editable=True)

    def __str__(self):
        return '#'+self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TagModel, self).save(*args, **kwargs)



class PostModel(models.Model):
    post_owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE, default=1,verbose_name="Post sahibi")
    subCategory = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE,default=1, related_name="subCategory_in_post", verbose_name='Alt Kategori', help_text="Post'un kategorisini seçiniz.")
    title = models.CharField(max_length=300,blank=False,verbose_name='Post Adı')
    subTitle = models.CharField(max_length=500, blank=True,null=True,verbose_name="Post alt başlığı", help_text='Postun alt başlığını giriniz.')
    text = RichTextUploadingField(blank=False,verbose_name="Post Yazısı", help_text='Postun yazısını giriniz.',config_name='awesome_ckeditor')
    read_time = models.CharField(default="0",max_length=5,blank=False,verbose_name='Gönderi Okuma Süresi',editable=True)
    tag = models.ManyToManyField(TagModel, blank=True, related_name="postsTag",verbose_name='Post Etiketleri ', help_text='Postun etiketlerini seçiniz.')
    image = models.ImageField(blank=True, null=True, default='static/light_logo.png',upload_to='blog/post/', verbose_name="Post Fotoğrafı ", help_text='Postun resmini seçiniz.')
    created_date = models.DateTimeField(editable=True,auto_now_add=False,default=datetime.now,blank=False, null=False, verbose_name="Post oluşturulma tarihi")
    modified_date = models.DateTimeField(editable=True,auto_now_add=False,auto_now=True,blank=False, null=False, verbose_name="Post güncelleme tarihi")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,editable=True,related_name="post_likes",verbose_name="Postu beğenenler",null=True,blank=True) 
    slug = models.SlugField(max_length=200,unique=True,editable=True,blank=True,null=True)

    def __str__(self):
        return self.post_owner.username+ ' : "' + self.title + '"'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
        self.slug = slugify(self.title)
        self.read_time = self.calc_read_time(self.text)
        super(PostModel, self).save(*args, **kwargs)
        self.slug = slugify(self.title+"-"+str(self.id))
        
        image = Image.open(self.image.path)        
        if image.height < 350 or image.width < 650 :
            new_size = (650,350)
            image.thumbnail(new_size)
            image.save(self.image.path)

        return super(PostModel, self).save(*args, **kwargs)


    def postUserProfile(self):
        allUsers_Q =  StudentUserProfileModel.objects.raw("Select id,user_id from studentUsers_studentuserprofilemodel where user_id = %s",[self.post_owner_id])
        for user in allUsers_Q:
            return user

    def likedPost(self):
        liked = False
        likes_Q =  StudentUserProfileModel.objects.raw("Select * from posts_postmodel_likes where postmodel_id = %s",[self.id])
        if likes_Q:
            liked = True
        return liked

    def calc_read_time(self,val):
        word_count = len(val.split())
        read_time = round((word_count/160))
        return read_time
        







# MİNİ POST MODELs DESİGNS


class MiniPostTagModel(models.Model):
    title = models.CharField(max_length=50, blank=False, verbose_name="Etiket adı")
    color = ColorField(default='#FF0000')
    slug = models.SlugField(default="emptySlug", editable=True)

    def __str__(self):
        return '#'+self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MiniPostTagModel, self).save(*args, **kwargs)

    

class MiniPostModel(models.Model):
    post_owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE, default=1,verbose_name="Mini post sahibi",null=True, blank=True)
    text = models.TextField(blank=True,null=True,verbose_name="Mini post Yazısı", help_text='Mini postun yazısını giriniz.')
    tag = models.ManyToManyField(MiniPostTagModel, blank=True, related_name="miniPostTag",verbose_name='Mini post etiketleri ', help_text='Mini postun etiketlerini seçiniz.')
    image = models.ImageField(blank=True, null=True,upload_to='blog/mini_posts/', verbose_name="Mini post fotoğrafı ", help_text='Mini postun resmini seçiniz.')
    created_date = models.DateTimeField(editable=True,auto_now_add=False,default=datetime.now,blank=False, null=False, verbose_name="Mini post oluşturulma tarihi")
    modified_date = models.DateTimeField(editable=True,auto_now_add=False,auto_now=True,blank=False, null=False, verbose_name="Mini post güncelleme tarihi")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,editable=True,related_name="miniPostLikes",verbose_name="Mini postu beğenenler",null=True,blank=True) 
    slug = models.SlugField(max_length=200,unique=True,editable=True,blank=True,null=True)


    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:7px; box-shadow: 0 16px 38px -12px rgb(0 0 0 / 56%), 0 4px 25px 0px rgb(0 0 0 / 12%), 0 8px 10px -5px rgb(0 0 0 / 20%); " />'.format(self.image.url))
        return "None Image"


    def __str__(self):
        return self.post_owner.username+ ' : "' + self.text[:100] + '"'


    def save(self, *args, **kwargs):
        super(MiniPostModel, self).save(*args, **kwargs)
        self.slug = slugify(self.post_owner.username+"-"+str(self.id))


    def likedPost(self):
        liked = False
        likes_Q =  StudentUserProfileModel.objects.raw("Select * from posts_minipostmodel_likes where minipostmodel_id = %s",[self.id])
        if likes_Q:
            liked = True
        return liked

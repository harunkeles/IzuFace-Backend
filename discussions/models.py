from datetime import datetime
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from colorfield.fields import ColorField
from sqlalchemy import null

from studentUsers.models import StudentUserProfileModel



class MainCategoryModel(models.Model):
    title = models.CharField(max_length=50, blank=False, verbose_name="Kategori Adı")
    slug = models.SlugField(default="emptySlug", editable=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MainCategoryModel, self).save(*args, **kwargs)


class TopicModel(models.Model):
    title = models.CharField(max_length=50, blank=False, verbose_name="Topik Adı")
    image = models.ImageField(blank=True, null=True, default='static/light_logo.png',upload_to='static/icons/discussions', verbose_name="Topik İkonu ", help_text='Topik ikonunu seçiniz.')
    slug = models.SlugField(default="emptySlug", editable=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TopicModel, self).save(*args, **kwargs)


class TagModel(models.Model):
    title = models.CharField(max_length=30, blank=False, verbose_name="Etiket adı")
    color = ColorField(default='#FF0000')
    slug = models.SlugField(default="emptySlug", editable=True)

    def __str__(self):
        return '#'+self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TagModel, self).save(*args, **kwargs)



class DiscussionsModel(models.Model):
    discussion_owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE, default=1,verbose_name="Tartışma sahibi")
    subCategory = models.ForeignKey(MainCategoryModel, on_delete=models.CASCADE,default=1, related_name="maincategory_in_discussion", verbose_name='Tartışma Kategorisi', help_text="Tartışmanın'un Kategorisini Seçiniz.")
    topic = models.ForeignKey(TopicModel, on_delete=models.CASCADE,default=1, related_name="topic_in_discussion", verbose_name='Topik Adı', help_text="Tartışmanın'un Topiğini Seçiniz.")
    title = models.CharField(max_length=300,blank=False,verbose_name='Tartışma Adı')
    text = RichTextUploadingField(blank=True, null=True, verbose_name="Tartışma Yazısı", help_text='Tartışma yazısını giriniz.',config_name='awesome_ckeditor')
    tag = models.ManyToManyField(TagModel, blank=True, related_name="discussionTag",verbose_name='Tartışma Etiketleri ', help_text='Tartışma etiketlerini seçiniz.')
    created_date = models.DateTimeField(editable=True,auto_now_add=False,default=datetime.now,blank=False, null=False, verbose_name="Tartışma oluşturulma tarihi")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,editable=True,related_name="discussion_likes",verbose_name="Tartışma beğenenler",null=True,blank=True) 
    slug = models.SlugField(max_length=200,unique=True,editable=True,blank=True,null=True)

    def __str__(self):
        return self.discussion_owner.username+ ' : "' + self.title + '"'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
        self.slug = slugify(self.title)
        super(DiscussionsModel, self).save(*args, **kwargs)
        self.slug = slugify(self.title+"-"+str(self.id))

        return super(DiscussionsModel, self).save(*args, **kwargs)


    def likedPost(self):
        liked = False
        likes_Q =  StudentUserProfileModel.objects.raw("Select * from posts_postmodel_likes where postmodel_id = %s",[self.id])
        if likes_Q:
            liked = True
        return liked
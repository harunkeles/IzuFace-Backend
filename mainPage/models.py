from django.db import models
from django.conf import settings
from django.db.models.base import Model
from multiselectfield import MultiSelectField
from django.template.defaultfilters import default, slugify
from PIL import Image
from django.db.models.signals import post_save
from mainPage.models import *
# Create your models here.



class MainPage(models.Model):
    birth_day = models.TextField(null=True,blank=True,verbose_name="Doğum Yılı")

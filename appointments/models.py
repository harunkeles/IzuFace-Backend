from datetime import datetime
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
import datetime
from multiselectfield import MultiSelectField


from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime



class AppointmentModel(models.Model):
    appointment_owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE, default=1,verbose_name="Randevu sahibi")
    APPOINTMENT_TYPE = (('Futbol', 'Futbol'),
              ('Golf', 'Golf'),
              )
    appointment_type = MultiSelectField(choices=APPOINTMENT_TYPE,null=True,blank=True,verbose_name="Randevu tipi")
    day = models.CharField(default="0",max_length=5,blank=False,verbose_name='Randevu günü',editable=True)
    month = models.CharField(default="0",max_length=5,blank=False,verbose_name='Randevu ayı',editable=True)
    hour = models.CharField(default="0",max_length=5,blank=False,verbose_name='Randevu saati',editable=True)
    created_date = models.DateTimeField(editable=True,auto_now_add=False,default=datetime.now,blank=False, null=False, verbose_name="Post oluşturulma tarihi")
    modified_date = models.DateTimeField(editable=True,auto_now_add=False,auto_now=True,blank=False, null=False, verbose_name="Post güncelleme tarihi")
    slug = models.SlugField(max_length=200,unique=True,editable=True,blank=True,null=True)

    def __str__(self):
        return str(self.appointment_owner.username)+ ' : "' + str(self.day) + '/"'+ str(self.month) + " - " + str(self.hour) + ':00'

    def save(self, *args, **kwargs):
        super(AppointmentModel, self).save(*args, **kwargs)
        self.slug = slugify(str(self.appointment_owner.username)+ ' : "' + str(self.day) + '/"'+ str(self.month) + " - " + str(self.hour))

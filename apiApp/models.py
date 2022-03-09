from django.db.models.deletion import CASCADE
from django.db import models
from django.conf import settings

# Create your models here.


class AuthUserSiteSettingsModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=CASCADE, default=1,verbose_name="Post sahibi")
    dark_theme = models.BooleanField(default=False, verbose_name="Koyu tema aiktif mi?",editable=True)

    def __str__(self) :
        return self.user.username
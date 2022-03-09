from django.contrib import admin
from .models import *


class AuthUserSiteSettingsAdmin(admin.ModelAdmin):
    list_filter = ('dark_theme',)
    list_display = ('__str__','dark_theme',)
    search_fields = ('dark_theme',)

    class Meta:
        model = AuthUserSiteSettingsModel

admin.site.register(AuthUserSiteSettingsModel, AuthUserSiteSettingsAdmin)

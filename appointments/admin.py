from django.contrib import admin
from .models import *

class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ('day','month','hour')
    list_display = ('__str__','created_date')
    search_fields = ('__str__',)

    class Meta:
        model = AppointmentModel


admin.site.register(AppointmentModel, AppointmentAdmin)

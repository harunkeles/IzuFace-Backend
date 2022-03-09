from django.contrib import admin
from .models import *



class SubCategoryAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)

    class Meta:
        model = NewsSubCategoryModel

class TagAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)

    class Meta:
        model = NewsTagModel

class PostAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('__str__','created_date','modified_date')
    search_fields = ('title',)

    class Meta:
        model = NewsPostModel

admin.site.register(NewsSubCategoryModel, SubCategoryAdmin)
admin.site.register(NewsTagModel, TagAdmin)
admin.site.register(NewsPostModel, PostAdmin)

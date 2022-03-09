from django.contrib import admin
from .models import *

class MainCategoryAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)

    class Meta:
        model = MainCategoryModel

class SubCategoryAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)

    class Meta:
        model = SubCategoryModel

class TagAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)

    class Meta:
        model = TagModel

class PostAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('__str__','created_date','modified_date')
    search_fields = ('title',)

    class Meta:
        model = PostModel

admin.site.register(MainCategoryModel, MainCategoryAdmin)
admin.site.register(SubCategoryModel, SubCategoryAdmin)
admin.site.register(TagModel, TagAdmin)
admin.site.register(PostModel, PostAdmin)

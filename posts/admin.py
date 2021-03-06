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


# Mini Post

class MiniPostAdmin(admin.ModelAdmin):
    list_filter = ('text',)
    list_display = ('thumbnail_preview','__str__','created_date','modified_date')
    search_fields = ('text',)

    class Meta:
        model = MiniPostModel

    #??? For displaying image in admin page
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
#/////////////////////////////////////////////

class MiniPostTagAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)

    class Meta:
        model = MiniPostTagModel



admin.site.register(MainCategoryModel, MainCategoryAdmin)
admin.site.register(SubCategoryModel, SubCategoryAdmin)
admin.site.register(TagModel, TagAdmin)
admin.site.register(PostModel, PostAdmin)
admin.site.register(MiniPostModel, MiniPostAdmin)
admin.site.register(MiniPostTagModel, MiniPostTagAdmin)

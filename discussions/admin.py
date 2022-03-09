from django.contrib import admin
from discussions.models import *

class MainCategoryAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)

    class Meta:
        model = MainCategoryModel

class TopicAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)

    class Meta:
        model = TopicModel

class TagAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title',)

    class Meta:
        model = TagModel

class DiscussionsAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('__str__','subCategory','topic','created_date')
    search_fields = ('title',)

    class Meta:
        model = DiscussionsModel

admin.site.register(MainCategoryModel, MainCategoryAdmin)
admin.site.register(TopicModel, TopicAdmin)
admin.site.register(TagModel, TagAdmin)
admin.site.register(DiscussionsModel, DiscussionsAdmin)

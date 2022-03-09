from django.contrib import admin
from .models import *
from django.contrib import messages
# Register your models here.


class StudentImageGalleryAdmin(admin.TabularInline):
    model = StudentImageGalleryModel
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

class StudentExperiencesAdmin(admin.TabularInline):
    model = StudentExperiencesModel
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

class StudentEducationsAdmin(admin.TabularInline):
    model = StudentEducationsModel
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

class StudentForeignLangAdmin(admin.TabularInline):
    model = StudentForeignLangModel
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

class StudentProgLangAdmin(admin.TabularInline):
    model = StudentProgLangModel
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

class StudentProgTalentAdmin(admin.TabularInline):
    model = StudentProgTalentModel
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

class StudentCertificatesAdmin(admin.TabularInline):
    model = StudentCertificatesModel
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

class StudentInterestedAdmin(admin.TabularInline):
    model = StudentInterestedModel
    extra = 1

    def get_extra (self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

@admin.register(StudentUserProfileModel)
class StudentUserProfileAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview','name_surname','__str__','active')
    search_fields = ('__str__',)
    # list_editable = ("studentId",)
    
#??? For displaying image in admin page
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
#/////////////////////////////////////////////

#??? For displaying active-pasif icon in admin page
    def active(self, obj):
        return obj.is_active == 1
    active.boolean = True
    
    def make_active(modeladmin, request, queryset):
        queryset.update(isActive = 1)
        messages.success(request, "Seçilen öğrenci(ler) ' Aktif ' olarak değiştirildi !!")
  
    def make_inactive(modeladmin, request, queryset):
        queryset.update(isActive = 0)
        messages.success(request, "Seçilen öğrenci(ler) ' Pasif ' olarak değiştirildi !!")
  
    admin.site.add_action(make_active, "Aktif Yap")
    admin.site.add_action(make_inactive, "Pasif Yap")
#/////////////////////////////////////////////

    inlines = [
        StudentImageGalleryAdmin,
        StudentExperiencesAdmin,
        StudentEducationsAdmin,
        StudentForeignLangAdmin,
        StudentProgLangAdmin,
        StudentProgTalentAdmin,
        StudentCertificatesAdmin,
        StudentInterestedAdmin
    ]


from statistics import mode
from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from django.template.defaultfilters import slugify
from PIL import Image
from django.db.models.signals import post_save
from apiApp.models import AuthUserSiteSettingsModel
from studentUsers.models import *
from django.utils.html import mark_safe
from rest_framework.authtoken.models import Token



class StudentUserProfileModel(models.Model):
    is_active = models.IntegerField(default=1,choices=((1,'Aktif'),(0,'Pasif')),verbose_name="Öğrenci aktif mi?")
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name="Profil Sahibi")
    studentId = models.CharField(max_length=9,null=True,blank=True,verbose_name="Öğrenci ID")
    backImage = models.ImageField(blank=True,null=True,default= 'static/bg.png',upload_to='studentUsers/background-image',verbose_name="Arka plan fotoğrafı")
    profImage = models.ImageField(blank=True,null=True,default= 'static/user-team.png',upload_to='studentUsers/profile-image',verbose_name="Profil fotoğrafı")
    departmentName = models.CharField(max_length=150,blank=True,null=True,verbose_name="Bölüm adı")
    smallDesc = models.TextField(default="İstanbul Sabahattin Zaim Üniversitesi öğrencisiyim.",max_length=500,null=True,blank=True,verbose_name="Kişinin kısa açıklaması")
    bioDesc = models.TextField(max_length=500,null=True,blank=True,verbose_name="Kişinin biografi açıklaması")
    departmentClass = models.CharField(max_length=1,null=True,blank=True,verbose_name="Sınıfı")
    phoneNumber = models.CharField(max_length=15,blank=True,null=True,verbose_name="Telefon numarası")
    adress = models.TextField(max_length=300,blank=True,null=True,verbose_name="Adres bilgisi")
    birth_day = models.DateField(null=True,blank=True,verbose_name="Doğum tarihi")
    STUDENT_USER_SELF_INFO = (('Doğum tarihi', 'Doğum tarihi'),
              ('Telefon', 'Telefon'),
              ('Açık adres', 'Açık adres')
              )
    studentUserSelfInfo = MultiSelectField(choices=STUDENT_USER_SELF_INFO,null=True,blank=True,verbose_name="Kişisel Bilgilerim \n( Sayfada görünmesini istediğiniz bilgileri seçiniz.)")
    instagram = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    github = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    whatsapp = models.URLField(null=True,blank=True)
    STUDENT_USER_SOCIAL_MEDIA = (('İnstagram', 'İnstagram'),
              ('Twitter', 'Twitter'),
              ('Facebook', 'Facebook'),
              ('Linkedn', 'Linkedn'),
              ('Github', 'Github'),
              ('Whatsapp', 'Whatsapp'),
              )
    studentUserSocialMedia = MultiSelectField(choices=STUDENT_USER_SOCIAL_MEDIA,null=True,blank=True,verbose_name="İletişim bilgileri")
    following = models.ManyToManyField(settings.AUTH_USER_MODEL,editable=True,related_name="following",verbose_name="Kullanıcının takip ettikleri",null=True,blank=True) 
    slug = models.SlugField(unique=True,editable=True)
    
    # USERNAME_FIELD = 'studentId'
    # REQUIRED_FIELDS = ['user.email']

    def __str__(self):
        return self.user.email

    def name_surname(self):
        return self.user.first_name +" "+ self.user.last_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.user.username+str(self.user.id))
        super(StudentUserProfileModel,self).save(*args,**kwargs)
        if self.studentId:
            self.slug = slugify(self.studentId)
            super(StudentUserProfileModel,self).save(*args,**kwargs)
        
        backImage = Image.open(self.backImage.path)        
        if backImage.height < 350 or backImage.width < 850 :
            new_size = (800,300)
            backImage.thumbnail(new_size)
            backImage.save(self.backImage.path)

        profImage = Image.open(self.profImage.path)        
        if profImage.height < 160 or profImage.width < 160 :
            new_size = (156,156)
            profImage.thumbnail(new_size)
            profImage.save(self.profImage.path)

    @property
    def thumbnail_preview(self):
        if self.profImage:
            return mark_safe('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:7px; box-shadow: 0 16px 38px -12px rgb(0 0 0 / 56%), 0 4px 25px 0px rgb(0 0 0 / 12%), 0 8px 10px -5px rgb(0 0 0 / 20%); " />'.format(self.profImage.url))
        return ""

    class Meta:
        verbose_name = 'Student Profile'

    def studentAllImagesGallery(self):
        return self.image_gallery_student_user.all()

    def studentExperiences(self):
        return self.experience_student_user.all()

    def studentEducations(self):
        return self.education_student_user.all()
        
    def studentForeignLang(self):
        return self.foreign_lang_student_user.all()
    
    def studentProgLang(self):
        return self.porgLang_student_user.all()
    
    def studentProgTalent(self):
        return self.porgTalent_student_user.all()

    def studentCertificates(self):
        return self.certificate_student_user.all()

    def studentInterested(self):
        return self.interested_student_user.all()

def create_user_profile(sender,instance,created,**kwargs):
    if created:
        StudentUserProfileModel.objects.create(user=instance)

post_save.connect(create_user_profile,sender=settings.AUTH_USER_MODEL)


def create_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

post_save.connect(create_token,sender=settings.AUTH_USER_MODEL)


def create_site_settings(sender,instance=None,created=False,**kwargs):
    if created:
        AuthUserSiteSettingsModel.objects.create(user=instance)

post_save.connect(create_site_settings,sender=settings.AUTH_USER_MODEL)


#! STUDENT-USER-IMAGE-GALLERY
def upload_image_gallery(instance, filename):
    return f"users/student-user/{instance.studentUser.user.email}/image-gallery/{filename}"

class StudentImageGalleryModel(models.Model):
    studentUser = models.ForeignKey(StudentUserProfileModel, on_delete=models.CASCADE, related_name="image_gallery_student_user")
    image = models.ImageField(upload_to=upload_image_gallery)
    imageDec = models.CharField(max_length=150,null=True,blank=True,verbose_name="Resim açıklaması")

    class Meta:
        verbose_name = 'Student >> Image Gallerie'


#! STUDENT-USER-EXPERIENCES
class StudentExperiencesModel(models.Model):
    studentUser = models.ForeignKey(StudentUserProfileModel,on_delete=models.CASCADE,related_name="experience_student_user")
    EXPERIENCE_INFO = (('İş Deneyimi', 'İş Deneyimi'), 
              ('Staj Deneyimi', 'Staj Deneyimi')
              )
    experienceInfo = MultiSelectField(choices=EXPERIENCE_INFO,blank=False,verbose_name="Deneyimi")
    startedDate = models.DateField(null=True,blank=True,verbose_name="Başlangıç tarihi")
    finishedDate = models.DateField(null=True,blank=True,verbose_name="Bitiş tarihi")
    companyName = models.CharField(max_length=100,null=True,blank=True,verbose_name="Şirket adı")
    experienceDesc = models.TextField(max_length=500,null=True,blank=True,verbose_name="İş deneyimi açıklaması")

    def __str__(self):
        return self.companyName
    
    class Meta:
        verbose_name = 'Student >> Experience'

    def monthCalculate(self):
        # return (datetime.datetime.now().month - self.finishedDate.month)
        return (self.finishedDate.month - self.startedDate.month)


#! STUDENT-USER-EDUCATIONS
class StudentEducationsModel(models.Model):
    studentUser = models.ForeignKey(StudentUserProfileModel,on_delete=models.CASCADE,related_name="education_student_user")
    EDUCATION_INFO = (('Lise', 'Lise'), 
              ('Üniversite', 'Üniversite'),
              ('Erasmus', 'Erasmus'),
              ('Yüksek Lisans', 'Yüksek Lisans'),
              ('Doktora', 'Doktora')
              )
    educationInfo = MultiSelectField(choices=EDUCATION_INFO,blank=False,verbose_name="Eğitimi")
    startedDate = models.DateField(null=True,blank=True,verbose_name="Başlangıç tarihi")
    finishedDate = models.DateField(null=True,blank=True,verbose_name="Bitiş tarihi")
    educationName = models.CharField(max_length=100,null=True,blank=True,verbose_name="Eğitim adı")
    educationPosition = models.CharField(max_length=100,null=True,blank=True,verbose_name="Eğitim pozisyon adı")
    educationDesc = models.TextField(max_length=500,null=True,blank=True,verbose_name="Eğitim açıklaması")

    def __str__(self):
        return self.educationName

    class Meta:
        verbose_name = 'Student >> Education'


#! STUDENT-USER-FOREIGN-LANG
class StudentForeignLangModel(models.Model):
    studentUser = models.ForeignKey(StudentUserProfileModel,on_delete=models.CASCADE,related_name="foreign_lang_student_user")
    FOREING_LANG_INFO = (('A1', 'A1'), 
              ('A2', 'A2'),
              ('B1', 'B1'),
              ('B2', 'B2'),
              ('C1', 'C1'),
              ('C2', 'C2')
              )
    langName = models.CharField(max_length=100,null=True,blank=True,verbose_name="Yabancı dil adı")
    foreignLangRank = MultiSelectField(choices=FOREING_LANG_INFO,blank=False,verbose_name="Yabancı dil derecesi")
    langDesc = models.TextField(max_length=500,null=True,blank=True,verbose_name="Yabancı dil açıklaması")

    def __str__(self):
        return self.langName

    class Meta:
        verbose_name = 'Student >> Foreign Language'

    def foreignRank(self):
        return int(self.foreignLangRank[0])+1
    
    def rankCount(self):
        return 5 - int(self.foreignLangRank[0])
         

#! STUDENT-PROG-LANG
class StudentProgLangModel(models.Model):
    studentUser = models.ForeignKey(StudentUserProfileModel,on_delete=models.CASCADE,related_name="porgLang_student_user")
    PROGLANG_RANK_INFO = (('0', '0'), 
              ('10', '10'),
              ('20', '20'),
              ('30', '30'),
              ('40', '40'),
              ('50', '50'),
              ('60', '60'),
              ('70', '70'),
              ('80', '80'),
              ('90', '90'),
              ('100', '100')
              )
    progLangRankInfo = MultiSelectField(choices=PROGLANG_RANK_INFO,blank=False,verbose_name="Programlama dili derecesi")
    progLangName = models.CharField(max_length=100,null=True,blank=True,verbose_name="Programlama dili adı")
    progLangDesc = models.TextField(max_length=500,null=True,blank=True,verbose_name="Programlama dili açıklaması")

    def __str__(self):
        return self.progLangName

    class Meta:
        verbose_name = 'Student >> Programming Language'

#! STUDENT-PROGGRAMS-TALENT
class StudentProgTalentModel(models.Model):
    studentUser = models.ForeignKey(StudentUserProfileModel,on_delete=models.CASCADE,related_name="porgTalent_student_user")
    PROGTALENT_RANK_INFO = (('0', '0'), 
              ('10', '10'),
              ('20', '20'),
              ('30', '30'),
              ('40', '40'),
              ('50', '50'),
              ('60', '60'),
              ('70', '70'),
              ('80', '80'),
              ('90', '90'),
              ('100', '100')
              )
    progTalentRankInfo = MultiSelectField(choices=PROGTALENT_RANK_INFO,blank=False,verbose_name="Program derecesi")
    progTalentName = models.CharField(max_length=100,null=True,blank=True,verbose_name="Program adı")
    progTalentDesc = models.TextField(max_length=500,null=True,blank=True,verbose_name="Program açıklaması")

    def __str__(self):
        return self.progTalentName

    class Meta:
        verbose_name = 'Student >> Programs Talent'


#! STUDENT-USER-CERTIFICATE-GALLERY
def upload_certificate_image(instance, filename):
    return f"users/student-user/{instance.studentUser.user.email}/certificate-images/{filename}"

class StudentCertificatesModel(models.Model):
    studentUser = models.ForeignKey(StudentUserProfileModel, on_delete=models.CASCADE, related_name="certificate_student_user")
    image = models.ImageField(upload_to=upload_certificate_image)
    imageDec = models.CharField(max_length=150,null=True,blank=True,verbose_name="Sertifika açıklaması")

    class Meta:
        verbose_name = 'Student >> Certificate'


#! STUDENT-USER-INTERESTED
class StudentInterestedModel(models.Model):
    studentUser = models.ForeignKey(StudentUserProfileModel,on_delete=models.CASCADE,related_name="interested_student_user")
    interestName = models.CharField(max_length=100,null=True,blank=True,verbose_name="İlgi adı")

    def __str__(self):
        return self.interestName

    class Meta:
        verbose_name = 'Student >> Interested'





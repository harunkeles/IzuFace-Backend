from rest_framework import serializers
from news.models import NewsPostModel,NewsSubCategoryModel,NewsTagModel
from studentUsers.models import StudentUserProfileModel


class NewsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['post_owner'] = instance.post_owner.first_name + " " + instance.post_owner.last_name
        representation['subCategory'] = instance.subCategory.title
        return representation

    class Meta:
        model = NewsPostModel
        fields = '__all__'


class NewsWithFilterSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # post owner user full name and image field
        instance_post_owner = StudentUserProfileModel.objects.all().filter(user = instance.post_owner.id).first()


        representation['post_owner'] = instance.post_owner.first_name + " " + instance.post_owner.last_name
        representation['subCategory'] = instance.subCategory.title

        list = []
        insTag = [val for val in NewsTagModel.objects.all() if val in instance.tag.all()]
        for i in range(instance.tag.count()):
            
            list.append((insTag[i].title,insTag[i].color))
        representation['tag'] = list



        representation['post_owner'] = {
            "id" : instance.post_owner.id,
            "full_name" : instance.post_owner.first_name + " " + instance.post_owner.last_name,
            "username" : instance.post_owner.username,
            "profImage" : str(instance_post_owner.profImage),
            "studentId" : str(instance_post_owner.studentId),
            "backImage" : str(instance_post_owner.backImage),
            "departmentName" : str(instance_post_owner.departmentName),
            "smallDesc" : str(instance_post_owner.smallDesc),
            "bioDesc" : str(instance_post_owner.bioDesc),
            "departmentClass" : str(instance_post_owner.departmentClass),
            "phoneNumber" : str(instance_post_owner.phoneNumber),
            "adress" : str(instance_post_owner.adress),
            "studentUserSelfInfo" : str(instance_post_owner.studentUserSelfInfo),
            "instagram" : str(instance_post_owner.instagram),
            "twitter" : str(instance_post_owner.twitter),
            "github" : str(instance_post_owner.github),
            "linkedin" : str(instance_post_owner.linkedin),
            "facebook" : str(instance_post_owner.facebook),
            "whatsapp" : str(instance_post_owner.whatsapp),
            "studentUserSocialMedia" : str(instance_post_owner.studentUserSocialMedia),
        }

        

        return representation


    class Meta:
        model = NewsPostModel
        fields = ['id','title','subTitle','image','created_date','post_owner','subCategory','tag']


class NewsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSubCategoryModel
        fields = ['id','title']
            
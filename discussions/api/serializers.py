from rest_framework import serializers
from discussions.models import DiscussionsModel, MainCategoryModel,TagModel, TopicModel
from studentUsers.models import StudentUserProfileModel


class DiscussionsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)

         # discussion owner user full name and image field
        instance_discussion_owner = StudentUserProfileModel.objects.all().filter(user = instance.discussion_owner.id).first()
        representation['discussion_owner'] = {
            "id" : instance.discussion_owner.id,
            "full_name" : instance.discussion_owner.first_name + " " + instance.discussion_owner.last_name,
            "profImage" : str(instance_discussion_owner.profImage),
            "studentId" : str(instance_discussion_owner.studentId),
            "backImage" : str(instance_discussion_owner.backImage),
            "departmentName" : str(instance_discussion_owner.departmentName),
            "smallDesc" : str(instance_discussion_owner.smallDesc),
            "bioDesc" : str(instance_discussion_owner.bioDesc),
            "departmentClass" : str(instance_discussion_owner.departmentClass),
            "phoneNumber" : str(instance_discussion_owner.phoneNumber),
            "adress" : str(instance_discussion_owner.adress),
            "studentUserSelfInfo" : str(instance_discussion_owner.studentUserSelfInfo),
            "instagram" : str(instance_discussion_owner.instagram),
            "twitter" : str(instance_discussion_owner.twitter),
            "github" : str(instance_discussion_owner.github),
            "linkedin" : str(instance_discussion_owner.linkedin),
            "facebook" : str(instance_discussion_owner.facebook),
            "whatsapp" : str(instance_discussion_owner.whatsapp),
            "studentUserSocialMedia" : str(instance_discussion_owner.studentUserSocialMedia),
        }


        # discussion category
        instance_discussion_category = MainCategoryModel.objects.all().filter(id = instance.subCategory.id).first()
        representation['subCategory'] = str(instance_discussion_category)
        

        # discussion topics
        instance_discussion_topic = TopicModel.objects.all().filter(id = instance.topic.id).first()
        representation['topic'] = {
            'name' : str(instance_discussion_topic),
            'image' : str(instance_discussion_topic.image)
            }
        

        return representation

    class Meta:
        model = DiscussionsModel
        fields = '__all__'


class DiscussionsDetailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # post owner user full name and image field
        instance_discussion_owner = StudentUserProfileModel.objects.all().filter(user = instance.discussion_owner.id).first()
        representation['discussion_owner'] = {
            "id" : instance.discussion_owner.id,
            "full_name" : instance.discussion_owner.first_name + " " + instance.discussion_owner.last_name,
            "profImage" : str(instance_discussion_owner.profImage),
            "created_date" : str(instance.discussion_owner.date_joined),
            "studentId" : str(instance_discussion_owner.studentId),
            "backImage" : str(instance_discussion_owner.backImage),
            "departmentName" : str(instance_discussion_owner.departmentName),
            "smallDesc" : str(instance_discussion_owner.smallDesc),
            "bioDesc" : str(instance_discussion_owner.bioDesc),
            "departmentClass" : str(instance_discussion_owner.departmentClass),
            "phoneNumber" : str(instance_discussion_owner.phoneNumber),
            "adress" : str(instance_discussion_owner.adress),
            "studentUserSelfInfo" : str(instance_discussion_owner.studentUserSelfInfo),
            "instagram" : str(instance_discussion_owner.instagram),
            "twitter" : str(instance_discussion_owner.twitter),
            "github" : str(instance_discussion_owner.github),
            "linkedin" : str(instance_discussion_owner.linkedin),
            "facebook" : str(instance_discussion_owner.facebook),
            "whatsapp" : str(instance_discussion_owner.whatsapp),
            "studentUserSocialMedia" : str(instance_discussion_owner.studentUserSocialMedia),
        }

        # discussion category
        instance_discussion_category = MainCategoryModel.objects.all().filter(id = instance.subCategory.id).first()
        representation['subCategory'] = str(instance_discussion_category)

        # discussion topics
        instance_discussion_topic = TopicModel.objects.all().filter(id = instance.topic.id).first()
        representation['topic'] = {
            'name' : str(instance_discussion_topic),
            'image' : str(instance_discussion_topic.image)
            }

        # tag title and tag color fields
        tags = {}
        tag_list = []
        tag_count = instance.tag.count()
        instance_tag = [val for val in TagModel.objects.all() if val in instance.tag.all()]
        for i in range(tag_count):
            tags.setdefault(instance_tag[i].title,instance_tag[i].color) 

        for key in tags:
            tag_list.append((key, tags[key]))

        representation['tag'] = tag_list

        return representation



    class Meta:
        model = DiscussionsModel
        fields = '__all__'




class MainCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategoryModel
        fields = ['id','title']


class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = ['id','title','image']
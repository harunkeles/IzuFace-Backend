from rest_framework import serializers
from posts.models import MiniPostModel, MiniPostTagModel, PostModel, MainCategoryModel,TagModel
from studentUsers.models import StudentUserProfileModel
from rest_framework.response import Response

class PostsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['post_owner'] = instance.post_owner.first_name + " " + instance.post_owner.last_name
        representation['subCategory'] = instance.subCategory.title
        return representation

    class Meta:
        model = PostModel
        fields = '__all__'



class PostDetailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # post owner user full name and image field
        instance_post_owner = StudentUserProfileModel.objects.all().filter(user = instance.post_owner.id).first()

       # We find the following
        following_this_user =  StudentUserProfileModel.objects.raw("Select * from studentUsers_studentuserprofilemodel_following where studentuserprofilemodel_id = %s",[instance.post_owner.id])
        following_list = []
        for i in range(len(list(following_this_user))):
            all_following_this_user = StudentUserProfileModel.objects.filter(id = following_this_user[i].user_id)
            following_list.append(all_following_this_user[0].id)

        # We find the followers count
        followers =  StudentUserProfileModel.objects.raw("Select * from studentUsers_studentuserprofilemodel_following where user_id = %s",[instance.post_owner.id])
        followers_count = len(list(followers))

        representation['post_owner'] = {
            "id" : instance.post_owner.id,
            "full_name" : instance.post_owner.first_name + " " + instance.post_owner.last_name,
            "profImage" : str(instance_post_owner.profImage),
            "created_date" : instance.post_owner.date_joined,
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
            "following" : following_list,
            "followers": followers_count,
        }

        # post sub category name field
        representation['subCategory'] = instance.subCategory.title

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
        model = PostModel
        fields = '__all__'



class PostsWithFilterSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # post owner user full name and image field
        instance_post_owner = StudentUserProfileModel.objects.all().filter(user = instance.post_owner.id).first()

        # We find the following
        following_this_user =  StudentUserProfileModel.objects.raw("Select * from studentUsers_studentuserprofilemodel_following where studentuserprofilemodel_id = %s",[instance.post_owner.id])
        following_list = []
        for i in range(len(list(following_this_user))):
            all_following_this_user = StudentUserProfileModel.objects.filter(id = following_this_user[i].user_id)
            following_list.append(all_following_this_user[0].id)


         # We find the followers count
        followers =  StudentUserProfileModel.objects.raw("Select * from studentUsers_studentuserprofilemodel_following where user_id = %s",[instance.post_owner.id])
        followers_count = len(list(followers))

            
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
            "following" : following_list,
            "followers": followers_count,
        }

        # post sub category name field
        representation['subCategory'] = instance.subCategory.title

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
        model = PostModel
        fields = ['id','title','subTitle','image','created_date','modified_date','read_time','post_owner','subCategory','tag','likes']
        


class PostsWithUserRelatedPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['id','title','image','post_owner']
        




class MainCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategoryModel
        fields = ['id','title']




# Mini Posts



class AllMiniPostTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniPostTagModel
        fields = '__all__'



class MiniPostsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['post_owner'] = instance.post_owner.first_name + " " + instance.post_owner.last_name

        # tag title and tag color fields
        tags = {}
        tag_list = []
        tag_count = instance.tag.count()
        instance_tag = [val for val in MiniPostTagModel.objects.all() if val in instance.tag.all()]
        for i in range(tag_count):
            tags.setdefault(instance_tag[i].title,instance_tag[i].color) 

        for key in tags:
            tag_list.append((key, tags[key]))

        representation['tag'] = tag_list


        return representation

    class Meta:
        model = MiniPostModel
        fields = '__all__'


class MiniPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniPostModel
        fields = '__all__'

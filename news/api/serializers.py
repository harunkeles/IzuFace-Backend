from rest_framework import serializers
from news.models import NewsPostModel,NewsSubCategoryModel,NewsTagModel


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
        representation['post_owner'] = instance.post_owner.first_name + " " + instance.post_owner.last_name
        representation['subCategory'] = instance.subCategory.title

        list = []
        insTag = [val for val in NewsTagModel.objects.all() if val in instance.tag.all()]
        for i in range(instance.tag.count()):
            list.append(insTag[i].title)
        representation['tag'] = list

        return representation


    class Meta:
        model = NewsPostModel
        fields = ['id','title','subTitle','image','created_date','post_owner','subCategory','tag']


class NewsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSubCategoryModel
        fields = ['id','title']
            
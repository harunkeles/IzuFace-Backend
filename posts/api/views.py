from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from slugify import slugify
from posts.models import MiniPostModel, MiniPostTagModel, PostModel, MainCategoryModel
from .serializers import AllMiniPostTagsSerializer, MiniPostCreateSerializer, MiniPostsSerializer, PostDetailSerializer, PostsSerializer, MainCategoriesSerializer, PostsWithFilterSerializer, PostsWithUserRelatedPostsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core.files import File


class PostsListView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostsSerializer


class PostsWithFilterListView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostsWithFilterSerializer


class PostsWithFilterDetailView(RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostsWithFilterSerializer


class PostsWithUserRelatedPostsView(ListAPIView):
    queryset = PostModel.objects.all()
    User = get_user_model()
    serializer_class = PostsWithUserRelatedPostsSerializer

    def get(self, request, pk=None, *args, **kwargs):
        related_posts = PostModel.objects.filter(post_owner_id=pk)
        related_posts_list = []
        related_user = self.User.objects.filter(id=pk).first()

        for i in range(len(related_posts)):
            post = {
                'id': related_posts[i].id,
                'title': related_posts[i].title,
                'image': str(related_posts[i].image),
            }
            related_posts_list.append(post)

        return Response({
            'related_posts': {
                'related_user': {
                    'id': related_user.id,
                    'first_name': related_user.first_name,
                    'last_name': related_user.last_name,
                },
                'related_posts_list': related_posts_list,
            }
        })


class GetLastPostsListView(ListAPIView):
    serializer_class = PostsSerializer

    def get_queryset(self):
        num = self.kwargs['pk']
        return PostModel.objects.all().order_by('-id')[:num]


class PostDetailView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostDetailSerializer


class MainCategoriesListView(ListCreateAPIView):
    queryset = MainCategoryModel.objects.all()
    serializer_class = MainCategoriesSerializer


#!! Mini Post

# List Get
class AllMiniPostTagsListView(ListAPIView):
    queryset = MiniPostTagModel.objects.all()
    serializer_class = AllMiniPostTagsSerializer


# List Get
class MiniPostsListView(ListAPIView):
    queryset = MiniPostModel.objects.all()
    serializer_class = MiniPostsSerializer


# Single Delete Update
class MiniPostsUdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = MiniPostModel.objects.all()
    serializer_class = MiniPostsSerializer


# Single Create
class MiniPostsCreateView(CreateAPIView):
    queryset = MiniPostModel.objects.all()
    serializer_class = MiniPostCreateSerializer

    def post(self, request, *args, **kwargs):

        print(request.data)
        print(request.data["image"])

        # Tag listesini buluyoruz.
        tag = request.data["tag"]
        print("tag : " , tag)

        tag_list = []
        for i in list(tag):
            if i != ',' :
                print(i)
                tag_list.append(int(i))
        
        print("tag_list : " , tag_list)

        # Eklenecek olan data'yı response'dan aldım ve objemi oluşturdum
        miniPostModel = MiniPostModel.objects.create(
            post_owner=request.user,
            text=request.data["text"],
            image=request.data["image"],
        )

        # İlk önce objemi tag'lar olmadan kaydettim.
        miniPostModel.save()
        # Eklenmiş objemi güncelledim
        miniPostModel.tag.set(tag_list)

        return Response({
            "id": miniPostModel.id,
            "text": miniPostModel.text,
            "image": str(miniPostModel.image),
            "created_date": miniPostModel.created_date,
            "modified_date": miniPostModel.modified_date,
            "slug": miniPostModel.slug,
            "post_owner": miniPostModel.post_owner.first_name + " " + miniPostModel.post_owner.last_name,
            "tag": tag_list,
        })

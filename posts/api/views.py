from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from slugify import slugify
from posts.models import MiniPostModel, MiniPostTagModel, PostModel, MainCategoryModel
from sentiment import sentiment
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


class MiniPostsWithCategoryListView(ListAPIView):
    queryset = MiniPostModel.objects.all()
    serializer_class = MiniPostsSerializer

    def get(self, request, pk=None, *args, **kwargs):
        mini_posts = MiniPostModel.objects.filter(category=pk)

        mini_posts_list = []
        for i in range(len(mini_posts)):
            post = {
                'id': mini_posts[i].id,
                'text': mini_posts[i].text,
                'image': str(mini_posts[i].image),
                'created_date': mini_posts[i].created_date,
                'category': mini_posts[i].category,
            }
            mini_posts_list.append(post)

        return Response({
            "mini_posts": mini_posts_list
        })


# Single Delete Update
class MiniPostsUdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = MiniPostModel.objects.all()
    serializer_class = MiniPostsSerializer


# Single Create
class MiniPostsCreateView(CreateAPIView):
    queryset = MiniPostModel.objects.all()
    serializer_class = MiniPostCreateSerializer

    def post(self, request, *args, **kwargs):

        # Tag listesini buluyoruz.
        tag = request.data["tag"]

        tag_list = []
        for i in list(tag):
            if i != ',':
                tag_list.append(int(i))


        #Sentiment Analiz
        sentimentA = sentiment(request.data["text"])

        # Eklenecek olan data'y?? response'dan ald??m ve objemi olu??turdum
        miniPostModel = MiniPostModel.objects.create(
            post_owner=request.user,
            category=sentimentA,
            text=request.data["text"],
            image=request.data["image"],
        )

        # ??lk ??nce objemi tag'lar olmadan kaydettim.
        miniPostModel.save()
        # Eklenmi?? objemi g??ncelledim
        miniPostModel.tag.set(tag_list)

        return Response({
            "id": miniPostModel.id,
            "text": miniPostModel.text,
            "image": str(miniPostModel.image),
            "category": miniPostModel.category,
            "created_date": miniPostModel.created_date,
            "modified_date": miniPostModel.modified_date,
            "slug": miniPostModel.slug,
            "post_owner": miniPostModel.post_owner.first_name + " " + miniPostModel.post_owner.last_name,
            "tag": tag_list,
        })


class SingleUserMiniPostsListView(ListAPIView):
    queryset = MiniPostModel.objects.all()
    User = get_user_model()
    serializer_class = MiniPostsSerializer

    def get(self, request, pk=None, *args, **kwargs):
        mini_posts = MiniPostModel.objects.filter(post_owner_id=pk)

        tags = MiniPostModel.objects.raw(
            "Select * from posts_minipostmodel_tag where minipostmodel_id = %s", [mini_posts[0].id])

        mini_posts_list = []
        tag_list = []

        for i in range(len(list(tags))):
            tag_prop = MiniPostTagModel.objects.filter(
                id=tags[i].miniposttagmodel_id)
            tag_list.append(tag_prop[0])

        for i in range(len(mini_posts)):
            post = {
                'id': mini_posts[i].id,
                'text': mini_posts[i].text,
                'image': str(mini_posts[i].image),
                'modified_date': mini_posts[i].modified_date,
                'text': mini_posts[i].text,
                # 'tag': (k for k in tag_list),
                # 'likes': mini_posts[i].likes,
            }
            mini_posts_list.append(post)

        return Response({
            "mini_posts": mini_posts_list
        })

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView,ListCreateAPIView
from posts.models import PostModel, MainCategoryModel
from .serializers import PostDetailSerializer, PostsSerializer, MainCategoriesSerializer,PostsWithFilterSerializer,PostsWithUserRelatedPostsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

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

    def get(self,request, pk=None,*args,**kwargs):
        related_posts = PostModel.objects.filter(post_owner_id=pk)
        related_posts_list = []
        related_user = self.User.objects.filter(id=pk).first()

        for i in range(len(related_posts)):
            post = {
                'id' : related_posts[i].id,
                'title' : related_posts[i].title,
                'image' : str(related_posts[i].image),
            }
            related_posts_list.append(post)

        
        return Response({
            'related_posts' : {
                'related_user' : {
                    'id' : related_user.id,
                    'first_name' : related_user.first_name,
                    'last_name' : related_user.last_name,
                },
                'related_posts_list' : related_posts_list,
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
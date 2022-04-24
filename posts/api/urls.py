from django.urls import path
from .views import  AllMiniPostTagsListView, MiniPostsCreateView, MiniPostsListView, MiniPostsUdateDeleteView, PostsListView, PostDetailView, MainCategoriesListView,PostsWithFilterListView,GetLastPostsListView,PostsWithFilterDetailView, PostsWithUserRelatedPostsView

urlpatterns = [
    
    path('', PostsListView.as_view()),
    path('post-with-filtered/', PostsWithFilterListView.as_view()),
    path('post-with-filtered/<int:pk>', PostsWithFilterDetailView.as_view()),
    path('last=<int:pk>/', GetLastPostsListView.as_view()),
    path('postId=<int:pk>/', PostDetailView.as_view()),
    path('related_posts/userId=<int:pk>/', PostsWithUserRelatedPostsView.as_view()),
    path('main-categories/', MainCategoriesListView.as_view()),


    path('mini-posts/', MiniPostsListView.as_view()),
    path('mini-posts/<int:pk>', MiniPostsUdateDeleteView.as_view()),
    path('mini-posts/create', MiniPostsCreateView.as_view()),
    path('mini-post-tags/', AllMiniPostTagsListView.as_view()),

]

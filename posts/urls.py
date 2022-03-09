from django.urls import path, include
from .views import *
from django.contrib.auth import views as authViews


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('all-posts/', AllPostView.as_view(), name='all_posts'),
    path('like/<int:pk>', LikeView, name='like_post'),

]

from django.urls import path, include
from .views import *
from django.contrib.auth import views as authViews


urlpatterns = [

    path('all-news/', NewsView.as_view(), name='all_news'),

]

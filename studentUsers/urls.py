from django.urls import path, include
from .views import *
from django.contrib.auth import views as authViews


urlpatterns = [

    path('myprofile/', StudentUserProfileView.as_view(), name='myprofile'),

]

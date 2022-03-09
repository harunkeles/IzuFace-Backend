from django.urls import path, include
from .views import *
from django.contrib.auth import views as authViews
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('', MainPageView.as_view(), name='mainPage'),

]
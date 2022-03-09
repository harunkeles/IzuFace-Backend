from django.urls import path

from apiApp.serializers import CustomAuthToken
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    path('all-users/', AllUserListView.as_view(), name='allUsers'),
    path('login/', CustomAuthToken.as_view(), name='authUser'),
    path('auth-user-info/<int:pk>-<str:url>',  AuthUserInfoView.as_view(), name='authUserInfo'),
    path('auth-user-site-settings/<int:pk>',  AuthUserSiteSettingsView.as_view(), name='authUserSiteSettings'),

]
urlpatterns = format_suffix_patterns(urlpatterns)

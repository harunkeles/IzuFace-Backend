from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from apiApp.models import AuthUserSiteSettingsModel
from studentUsers.models import StudentUserProfileModel


class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'



class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })



class AuthUserSiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserSiteSettingsModel
        fields = '__all__'



class UserRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUserProfileModel
        fields = '__all__'


class StudentUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUserProfileModel
        fields = '__all__'



class WithSameDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUserProfileModel
        fields = '__all__'

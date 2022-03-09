from rest_framework import serializers
from studentUsers.models import StudentUserProfileModel
from rest_framework.response import Response

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUserProfileModel
        fields = '__all__'


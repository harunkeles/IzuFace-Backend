from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView,ListCreateAPIView
from studentUsers.models import StudentUserProfileModel
from .serializers import StudentUserSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

class StudentUserView(RetrieveUpdateDestroyAPIView):
    queryset = StudentUserProfileModel.objects.all()
    serializer_class = StudentUserSerializer

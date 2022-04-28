from requests import delete
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from slugify import slugify
from appointments.models import AppointmentModel
from studentUsers.models import StudentUserProfileModel
from .serializers import AppointmentCreateSerializer, AppointmentSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django.core.files.storage import FileSystemStorage
from django.core.files import File


class AppointmentListView(ListAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentWithFilterAuthUserView(RetrieveUpdateDestroyAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer


class SingleUserAppointmentListView(ListAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer


    def get(self, request, pk=None, *args, **kwargs):

        user = StudentUserProfileModel.objects.filter(user=pk)

        appointment_owner_user = AppointmentModel.objects.filter(appointment_owner=pk)
        print("appointment_owner_user : " , appointment_owner_user)
        appointment_owner_user_list = []
        for i in range(len(list(appointment_owner_user))):
            appointmet = {
                "id" :appointment_owner_user[i].id,
                "appointment_type": appointment_owner_user[i].appointment_type[0],
                "day": appointment_owner_user[i].day,
                "month": appointment_owner_user[i].month,
                "hour": appointment_owner_user[i].hour,
                "created_date": appointment_owner_user[i].created_date,
                "modified_date": appointment_owner_user[i].modified_date,
                "appointment_owner": {
                    "id": appointment_owner_user[i].appointment_owner.id,
                    "full_name": appointment_owner_user[i].appointment_owner.first_name + " " + appointment_owner_user[i].appointment_owner.last_name,
                    "prof_img": str(user[i].profImage) 
                }
            }

            appointment_owner_user_list.append(appointmet)

        return Response(appointment_owner_user_list)




# Single Create
class AppointmentCreateView(CreateAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentCreateSerializer

    def post(self, request, *args, **kwargs):

        # Eklenecek olan data'yı response'dan aldım ve objemi oluşturdum
        appointmentModel = AppointmentModel.objects.create(
            appointment_owner=request.user,
            day=request.data["day"],
            month=request.data["month"],
            hour=request.data["hour"],
        )

        # İlk önce objemi tag'lar olmadan kaydettim.
        appointmentModel.save()

        return Response({
            "id": appointmentModel.id,
            "day": appointmentModel.day,
            "month": appointmentModel.month,
            "hour": appointmentModel.hour,
            "created_date": appointmentModel.created_date,
            "modified_date": appointmentModel.modified_date,
            "slug": appointmentModel.slug,
            "appointment_owner": appointmentModel.appointment_owner.first_name + " " + appointmentModel.appointment_owner.last_name,
        })




# Single Delete Update
class AppointmentUdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer
    
    def delete(self, request, data):
        
        data = str(data)
        day = ""
        month = ""
        hour = ""
        if len(str(data)) == 5:
            day =  "0" + data[0:1]
            month = data[1:3]
            hour = data[3:5]
        else : 
            day = data[0:2]
            month = data[2:4]
            hour = data[4:6]

        obj = AppointmentModel.objects.filter(day = day, month = month, hour = hour).first()
        obj.delete()
        return Response({})
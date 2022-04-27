from rest_framework import serializers
from appointments.models import AppointmentModel
from studentUsers.models import StudentUserProfileModel
from rest_framework.response import Response

class AppointmentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = StudentUserProfileModel.objects.filter(user=instance.appointment_owner)
        print("user : ", user)
        representation['appointment_ref'] = instance.day + instance.month + instance.hour 
        representation['appointment_owner'] = {
            "id" : instance.appointment_owner.id,
            "full_name" : instance.appointment_owner.first_name + " " + instance.appointment_owner.last_name,
            "prof_img": str(user[0].profImage) 
        }
        return representation

    class Meta:
        model = AppointmentModel
        fields = '__all__'




class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = '__all__'

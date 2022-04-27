from django.urls import path
from appointments.api.views import AppointmentCreateView, AppointmentListView, SingleUserAppointmentListView


urlpatterns = [
    
    path('', AppointmentListView.as_view()),
    path('<int:pk>', SingleUserAppointmentListView.as_view()),
    path('create/', AppointmentCreateView.as_view()),
]

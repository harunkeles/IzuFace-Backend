from django.urls import path
from .views import  StudentUserView

urlpatterns = [
    
    path('studentId=<int:pk>/', StudentUserView.as_view()),

]

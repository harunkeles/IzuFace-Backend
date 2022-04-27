from django.views.generic import CreateView,UpdateView,ListView,FormView
from .models import *


class AppointmentView(ListView):
    template_name = 'all-posts/all-posts.html'
    model = AppointmentModel
    context_object_name = 'allPageAllPosts_C'

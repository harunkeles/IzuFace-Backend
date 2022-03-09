from django.contrib.auth.models import User
from django.template.defaultfilters import title
import jsonify
from mainPage.models import MainPage
from django.views.generic import CreateView, UpdateView, ListView, FormView
from news.models import NewsPostModel
from posts.models import MainCategoryModel, PostModel
from studentUsers.models import StudentUserProfileModel
from .models import *
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, response
import json
# Create your views here.


@method_decorator(login_required(login_url='/login'), name="dispatch")
class MainPageView(ListView):
    template_name = 'main-page/mainPage.html'
    model = PostModel
    context_object_name = 'mainPageAllPosts_C'

    def get_queryset(self):
        return PostModel.objects.order_by('-id')

    def get_context_data(self, object_list=None, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs) 
        context['authUser_C'] = StudentUserProfileModel.objects.filter(user = self.request.user)
        context['newsPosts_C'] = NewsPostModel.objects.all()
        return context


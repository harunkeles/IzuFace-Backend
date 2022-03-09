from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import request,HttpRequest
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from studentUsers.models import *
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,FormView
from django.contrib.auth.views import LoginView, LogoutView, PasswordContextMixin
from .forms import *
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class RegisterView(CreateView):
    template_name = 'log/register.html'
    form_class = RegisterForm

    def get_success_url(self) :
        return reverse('myprofile')
       


class UserSignin(LoginView):
    template_name = 'log/login.html'

    def get_success_url(self):
        return reverse('myprofile')


class UserLogout(LogoutView):
    template_name = 'log/logout.html'

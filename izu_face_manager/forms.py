from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.forms import widgets
from studentUsers.models import *
from django.contrib.auth.models import User
from django.forms.fields import Field


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    

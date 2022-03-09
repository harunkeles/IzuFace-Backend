from django.views.generic import CreateView,UpdateView,ListView,FormView
from .models import *
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class NewsView(ListView):
    template_name = 'news-page/newsPage.html'
    model = NewsPostModel

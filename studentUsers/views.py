from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView,UpdateView,ListView,FormView,DetailView
from .models import *
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
# Create your views here.



@method_decorator(login_required(login_url='/login'), name="dispatch")
class StudentUserProfileView(ListView):
    template_name = 'profile-pages/student-profile-page/studentUsersProfile.html'
    model = StudentUserProfileModel
    context_object_name = 'studentUserProfile_C'

    def get_context_data(self, **kwargs) :
        context = super(StudentUserProfileView,self).get_context_data(**kwargs)
        context['one_studentUserProfile_C'] = StudentUserProfileModel.objects.get(user=self.request.user)
        return context



def FollowingView(request,pk):
    user = get_object_or_404(StudentUserProfileModel, id=request.POST.get('following_id'))
    following = False
    if user.following.filter(id=request.user.id).exists():
        user.following.remove(request.user)
        following = False
    else:
        user.following.add(request.user)
        following = True
    return HttpResponseRedirect(reverse('mainPage'))
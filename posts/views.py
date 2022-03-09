from django.http.response import HttpResponse, JsonResponse
from django.views.generic import CreateView,UpdateView,ListView,FormView
from studentUsers.models import StudentUserProfileModel
from .models import *
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


@method_decorator(login_required(login_url='/login'), name="dispatch")
class AllPostView(ListView):
    template_name = 'all-posts/all-posts.html'
    model = PostModel
    context_object_name = 'allPageAllPosts_C'

    def get_queryset(self):
        return PostModel.objects.order_by('-id')

    def get_context_data(self, object_list=None, **kwargs):
        context = super(AllPostView, self).get_context_data(**kwargs) 
        auth_user = StudentUserProfileModel.objects.filter(user = self.request.user)
        context['authUser_C'] = auth_user
        context['mainCategorries_C'] = MainCategoryModel.objects.all()
        return context


def LikeView(request,pk):
    post = get_object_or_404(PostModel, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('all_posts'))

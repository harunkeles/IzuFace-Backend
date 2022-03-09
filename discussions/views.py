from .models import *
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect



def LikeView(request,pk):
    discussion = get_object_or_404(DiscussionsModel, id=request.POST.get('discussion_id'))
    liked = False
    if discussion.likes.filter(id=request.user.id).exists():
        discussion.likes.remove(request.user)
        liked = False
    else:
        discussion.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('all_posts'))

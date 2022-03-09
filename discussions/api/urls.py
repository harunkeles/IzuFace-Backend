from django.urls import path
from .views import  DiscussionsListView,DiscussionsDetailView , MainCategoriesListView, TopicsListView

urlpatterns = [
    
    path('', DiscussionsListView.as_view()),
    path('<int:pk>', DiscussionsDetailView.as_view()),
    path('categories', MainCategoriesListView.as_view()),
    path('topics', TopicsListView.as_view()),

]

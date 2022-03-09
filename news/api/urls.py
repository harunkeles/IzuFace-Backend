from django.urls import path
from .views import  NewsListView, NewsDetailView, NewsCategoriesListView,GetLastNewsListView,NewsWithFilterListView

urlpatterns = [
    
    path('', NewsListView.as_view()),
    path('news-with-filtered/', NewsWithFilterListView.as_view()),
    path('newsId=<int:pk>/', NewsDetailView.as_view()),
    path('last=<int:pk>/', GetLastNewsListView.as_view()),
    path('categories/', NewsCategoriesListView.as_view()),

]

from rest_framework.generics import ListAPIView, RetrieveAPIView
from news.models import NewsPostModel,NewsSubCategoryModel
from .serializers import NewsSerializer, NewsCategoriesSerializer,NewsWithFilterSerializer

class NewsListView(ListAPIView):
    queryset = NewsPostModel.objects.all()
    serializer_class = NewsSerializer


class NewsWithFilterListView(ListAPIView):
    queryset = NewsPostModel.objects.all()
    serializer_class = NewsWithFilterSerializer


class GetLastNewsListView(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        num = self.kwargs['pk']
        return NewsPostModel.objects.all().order_by('-id')[:num]


class NewsDetailView(RetrieveAPIView):
    queryset = NewsPostModel.objects.all()
    serializer_class = NewsSerializer


class NewsCategoriesListView(ListAPIView):
    queryset = NewsSubCategoryModel.objects.all()
    serializer_class = NewsCategoriesSerializer
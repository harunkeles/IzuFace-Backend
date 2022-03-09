from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from discussions.models import DiscussionsModel, MainCategoryModel, TopicModel
from discussions.api.serializers import DiscussionsDetailSerializer, DiscussionsSerializer, MainCategoriesSerializer, TopicsSerializer



class DiscussionsListView(ListAPIView):
    queryset = DiscussionsModel.objects.all()
    serializer_class = DiscussionsSerializer


class DiscussionsDetailView(RetrieveUpdateAPIView):
    queryset = DiscussionsModel.objects.all()
    serializer_class = DiscussionsDetailSerializer


class MainCategoriesListView(ListCreateAPIView):
    queryset = MainCategoryModel.objects.all()
    serializer_class = MainCategoriesSerializer


class TopicsListView(ListCreateAPIView):
    queryset = TopicModel.objects.all()
    serializer_class = TopicsSerializer
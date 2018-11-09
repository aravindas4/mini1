from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response

from m2m import models as m2m_models
from m2m import serializers as m2m_serializers


class PublicationList(generics.ListCreateAPIView):
    queryset = m2m_models.Publication.objects.all()
    serializer_class = m2m_serializers.PublicationSerializer
    name = 'publications-list'


class PublicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = m2m_models.Publication.objects.all()
    serializer_class = m2m_serializers.PublicationSerializer
    name = 'publications-detail'


class ArticleList(generics.ListCreateAPIView):
    queryset = m2m_models.Article.objects.all()
    serializer_class = m2m_serializers.ArticleSerializer
    name = 'article-list'


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = m2m_models.Article.objects.all()
    serializers_class = m2m_serializers.ArticleSerializer
    name = 'article-detail'


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response({
        'article': reverse(ArticleList.name, request=request),
        'publication': reverse(PublicationList.name, request=request),
        })

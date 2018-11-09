from rest_framework import serializers

from m2m import models as m2m_models

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = m2m_models.Publication
        fields = ('id', 'title',)


class ArticleSerializer(serializers.ModelSerializer):
    publications = PublicationSerializer(many=True)

    class Meta:
        model = m2m_models.Article
        fields = ('id', 'headline', 'publications')

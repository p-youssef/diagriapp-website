from rest_framework import serializers
from .models import Plant, AboutCompany, Article, NewsItem

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = '__all__'

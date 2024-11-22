from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import AboutCompany, Article, NewsItem
from .serializers import AboutCompanySerializer, ArticleSerializer, NewsItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class NewsItemListAPIView(ListAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer

class NewsItemDetailAPIView(RetrieveAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer


class AboutCompanyAPIView(APIView):
    def get(self, request):
        about_company = AboutCompany.objects.first()
        if not about_company:
            return Response({"error": "About Company configuration is missing."}, status=404)
        serializer = AboutCompanySerializer(about_company)
        return Response(serializer.data)

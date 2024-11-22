from django.urls import path
from .views import ArticleListAPIView, ArticleDetailAPIView, NewsItemListAPIView, NewsItemDetailAPIView, AboutCompanyAPIView

urlpatterns = [
    path('articles/', ArticleListAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('news/', NewsItemListAPIView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsItemDetailAPIView.as_view(), name='news-detail'),
    path('about/', AboutCompanyAPIView.as_view(), name='about-company'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('',   home,   name='home'),
    path('about/',  about,  name='about'),
    path('news/', NewsItemsView.as_view(), name='news'),
    path('news-item/<int:pk>/', news_item, name='news_item'),
    
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('article/<int:pk>/', article, name='article'),

    path('favicon.ico', favicon, name='favicon'),

]


#handler404 = custom_404_view

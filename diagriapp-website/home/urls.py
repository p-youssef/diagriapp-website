from django.urls import path
from .views import *

urlpatterns = [
    path('home/',   home,   name='home'),
    path('about/',  about,  name='about'),
    path('news/', NewsItemsView.as_view(), name='news'),
    path('articles/', ArticlesView.as_view(), name='articles'),

]

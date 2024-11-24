from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    
    context = {
        'AboutCompany': AboutCompany.objects.all().first(),
    }
    return render(request, 'home.html', context)



def about(request):
    
    context = {
        'AboutCompany': AboutCompany.objects.all().first(),
    }
    return render(request, 'about.html', context)


class NewsItemsView(ListView):
    model = NewsItem
    template_name = 'news.html'
    context_object_name = 'items'
    paginate_by = 5  # This enables pagination
    ordering = ['-publish_time'] 

   


class ArticlesView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 5  # This enables pagination
    ordering = ['-release_date'] 

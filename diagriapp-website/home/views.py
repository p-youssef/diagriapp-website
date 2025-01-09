from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import FileResponse
from django.shortcuts import get_object_or_404, render
from .models import *
import os

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AboutCompany'] = AboutCompany.objects.all().first()
        return context

class ArticlesView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 5  # This enables pagination
    ordering = ['-release_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AboutCompany'] = AboutCompany.objects.all().first()
        return context


def news_item(request, pk):
    # Retrieve the NewsItem object or return a 404 if not found
    news_item = get_object_or_404(NewsItem, pk=pk)
    
    # Add AboutCompany to the context
    context = {
        'item': news_item,
        'AboutCompany': AboutCompany.objects.all().first(),
    }
    
    return render(request, 'news_item.html', context)


def article(request, pk):
    # Retrieve the NewsItem object or return a 404 if not found
    article = get_object_or_404(Article, pk=pk)
    
    # Add AboutCompany to the context
    context = {
        'item': article,
        'AboutCompany': AboutCompany.objects.all().first(),
    }
    
    return render(request, 'article.html', context)

def favicon(request):
    file_path = os.path.join('static', 'images', 'favicon.png')
    return FileResponse(open(file_path, 'rb'), content_type='image/x-icon')


from django.shortcuts import render

def custom_404_view(request, exception):
    print(2222)
    context = {
        
    }
    return render(request, '404.html', context, status=404)

from django.shortcuts import render
from blog_app.models import Article, Category
# Create your views here.

def home_page(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all()[0:3]
    return render(request, 'home_app/index.html', context={'articles':articles, 'recent_articles':recent_articles})


def sidebar_view(request):
    recent_articles = Article.objects.order_by('-created')
    categories = Category.objects.all()
    return render(request, 'includes/sidebar.html', context={'recent_articles':recent_articles, 'categories':categories})
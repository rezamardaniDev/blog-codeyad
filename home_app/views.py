from django.shortcuts import render
from blog_app.models import Article
# Create your views here.

def home_page(request):
    articles = Article.custome_manager.all()
    return render(request, 'home_app/index.html', context={'articles':articles})
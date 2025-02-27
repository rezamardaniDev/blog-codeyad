from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.urls import reverse

# Create your views here.
def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    print(reverse('blog:post-detail', args=[article.slug]))
    return render(request, 'blog_app/post_detail.html', context={'article':article})

def all_posts(request):
    articles = Article.objects.all()
    return render(request, 'blog_app/posts_list.html', context={'articles':articles})

def get_with_cat(request, cat):
    articles = Article.objects.filter(category__title=cat)
    return render(request, 'blog_app/posts_list.html', context={'articles':articles})
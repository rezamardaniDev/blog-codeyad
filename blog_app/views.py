from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.urls import reverse

# Create your views here.
def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    print(reverse('blog:post-detail', args=[article.slug]))
    return render(request, 'blog_app/post_detail.html', context={'article':article})
from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def post_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog_app/post_detail.html', context={'article':article})
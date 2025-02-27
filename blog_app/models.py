from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .managers import *
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70, help_text='enter title for post', unique=True)
    body  = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    
    # Managers
    objects = models.Manager()
    custome_manager = ArticleManager()
    
    class Meta:
        ordering = ['-updated']
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def get_url(self):
        return reverse('blog:post-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(args, kwargs)
    
    def __str__(self):
        return self.title
    
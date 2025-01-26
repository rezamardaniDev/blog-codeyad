from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())
    
    def published(self):
        return self.filter(is_published=True)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70, help_text='enter title for post', unique=True)
    body  = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    objects = ArticleManager()
    
    def save(self, *args, **kwargs):
        self.title = self.title.replace('*', '')
        super(Article, self).save(args, kwargs)
    
    def __str__(self):
        return self.title
    
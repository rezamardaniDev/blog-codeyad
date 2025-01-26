from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    
    def __str__(self):
        return self.title
    
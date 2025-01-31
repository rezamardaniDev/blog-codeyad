from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/<slug:slug>', views.post_detail, name='post-detail'),
    path('all', views.all_posts, name='all-post')
]

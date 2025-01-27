from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/<str:slug>', views.post_detail, name='post-detail')
]

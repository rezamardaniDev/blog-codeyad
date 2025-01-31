from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='index'),
    path('sidebar', views.sidebar_view, name='sidebar_partial')
]

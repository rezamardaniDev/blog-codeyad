from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register_page, name='register')
]

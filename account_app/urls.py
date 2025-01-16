from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup', views.signup_page, name='signup')
]

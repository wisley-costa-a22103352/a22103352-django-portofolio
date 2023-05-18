#  hello/urls.py

from django.urls import path
from . import views

app_name = 'portofolio'

urlpatterns = [
    path('home', views.home_page_view, name='home')
]
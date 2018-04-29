from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweets/', views.tweets, name='tweets'),
    path('tweets/create', views.create, name='create'),
]
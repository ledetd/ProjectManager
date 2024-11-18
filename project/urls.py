from django.contrib import admin
from django.urls import path
from .views import Index, Dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
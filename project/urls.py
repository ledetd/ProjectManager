from django.contrib import admin
from django.urls import path
from .views import Index, Dashboard, Crewboard, Wellboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('crewboard/', Crewboard.as_view(), name='crewboard'),
    path('wellboard/', Wellboard.as_view(), name='wellboard'),
]
from django.contrib import admin
from django.urls import path
from .views import Home



urlpatterns = [
    path('pra', Home.as_view(), name='projectreadiness-home'),
]
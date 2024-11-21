from django.contrib import admin
from django.urls import path
from .views import Index, Dashboard, Crewboard, Wellboard, Scheduleboard, Toolboard, Noteboard, Dayboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('crewboard/', Crewboard.as_view(), name='crewboard'),
    path('wellboard/', Wellboard.as_view(), name='wellboard'),
    path('scheduleboard/', Scheduleboard.as_view(), name='scheduleboard'),
    path('toolboard/', Toolboard.as_view(), name='toolboard'),
    path('noteboard/', Noteboard.as_view(), name='noteboard'),
    path('dayboard/', Dayboard.as_view(), name='dayboard'),
]
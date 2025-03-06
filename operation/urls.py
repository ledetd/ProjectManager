from django.contrib import admin
from django.urls import path
from .views import Home, Dashboard, AddProject, AddManager, AddAction



urlpatterns = [
    path('', Home.as_view(), name='operation-home'),
    path('operation/dashboard', Dashboard.as_view(), name='operation-dashboard'),
    path('operation/add-project', AddProject.as_view(), name='operation-add-project'),
    path('operation/add-project-manager', AddManager.as_view(), name='operation-add-project-manager'),
    path('operation/add-project-action', AddAction.as_view(), name='operation-add-project-action'),
]
from django.contrib import admin
from django.urls import path
from .views import SignUpView, Dashboard, AddItem, EditItem, DeleteItem, ConsumeableDashboard
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', Dashboard.as_view(), name='dashboard'),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('consumable-dashboard', ConsumeableDashboard.as_view(), name='consumable-dashboard'),
    path('add-item/', AddItem.as_view(), name='add-item'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='edit-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
]
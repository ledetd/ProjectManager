from django.contrib import admin
from django.urls import path
from .views import Index, Dashboard, Crewboard, Wellboard, Scheduleboard, Toolboard, AddTool, EditTool, Noteboard, AddNote, EditNote, Dayboard, AddDay, EditDay
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('crewboard/', Crewboard.as_view(), name='crewboard'),
    path('wellboard/', Wellboard.as_view(), name='wellboard'),
    path('scheduleboard/', Scheduleboard.as_view(), name='scheduleboard'),
    
    path('toolboard/', Toolboard.as_view(), name='toolboard'),
    path('add-tool/', AddTool.as_view(), name='add-tool'),
    path('edit-tool/<int:pk>', EditTool.as_view(), name='edit-tool'),   

    path('noteboard/', Noteboard.as_view(), name='noteboard'),
    path('add-note/', AddNote.as_view(), name='add-note'),
    path('edit-note/<int:pk>', EditNote.as_view(), name='edit-note'),

    path('dayboard/', Dayboard.as_view(), name='dayboard'),
    path('add-day/', AddDay.as_view(), name='add-day'),
    path('edit-day/<int:pk>', EditDay.as_view(), name='edit-day'),
]
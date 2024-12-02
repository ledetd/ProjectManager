from django.contrib import admin
from django.urls import path
from .views import Index, Dashboard, Crewboard, AddCrew, EditCrew, Wellboard, WellDetailView, AddWell, EditWell, Scheduleboard, Toolboard, AddTool, EditTool,Noteboard, AddNote, EditNote, Dayboard, AddDay, EditDay 
from .views import Spareboard, SpareDetailView, AddSpare, EditSpare, CrewDetailView, DeleteNote, Trackerboard, TrackerDetailView, AddTracker, EditTracker, Hercboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    path('crewboard/', Crewboard.as_view(), name='crewboard'),
    path("detail-crew/<int:pk>", CrewDetailView.as_view(), name="detail-crew"),
    path('add-crew/', AddCrew.as_view(), name='add-crew'),
    path('edit-crew/<int:pk>', EditCrew.as_view(), name='edit-crew'),   

    path('wellboard/', Wellboard.as_view(), name='wellboard'),
    path("detail-well/<int:pk>", WellDetailView.as_view(), name="detail-well"),
    path('add-well/', AddWell.as_view(), name='add-well'),
    path('edit-well/<int:pk>', EditWell.as_view(), name='edit-well'),   

    path('scheduleboard/', Scheduleboard.as_view(), name='scheduleboard'),
    
    path('spareboard/', Spareboard.as_view(), name='spareboard'),
    path("detail-spare/<int:pk>", SpareDetailView.as_view(), name="detail-spare"),
    path('add-spare/', AddSpare.as_view(), name='add-spare'),
    path('edit-spare/<int:pk>', EditSpare.as_view(), name='edit-spare'),   

    path('toolboard/', Toolboard.as_view(), name='toolboard'),
    path('add-tool/', AddTool.as_view(), name='add-tool'),
    path('edit-tool/<int:pk>', EditTool.as_view(), name='edit-tool'),   

    path('noteboard/', Noteboard.as_view(), name='noteboard'),
    path('add-note/', AddNote.as_view(), name='add-note'),
    path('edit-note/<int:pk>', EditNote.as_view(), name='edit-note'),
    path('delete-note/<int:pk>', DeleteNote.as_view(), name='delete-note'),

    path('dayboard/', Dayboard.as_view(), name='dayboard'),
    path('add-day/', AddDay.as_view(), name='add-day'),
    path('edit-day/<int:pk>', EditDay.as_view(), name='edit-day'),

    path('trackerboard/', Trackerboard.as_view(), name='trackerboard'),
    path("detail-tracker/<int:pk>", TrackerDetailView.as_view(), name="detail-tracker"),
    path('add-tracker/', AddTracker.as_view(), name='add-tracker'),
    path('edit-tracker/<int:pk>', EditTracker.as_view(), name='edit-tracker'),  
     
    path('hercboard/', Hercboard.as_view(), name='hercboard'), 

]
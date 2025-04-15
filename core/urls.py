
from django.contrib import admin
from django.urls import path, include

admin.site.site_title = "BEST"
admin.site.site_header = "Beyond Energy Project Manager"
admin.site.index_title = "BEST Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
]

from django.contrib import admin
from . models import Project, ProjectManager, Well

admin.site.register(Project)
admin.site.register(ProjectManager)
admin.site.register(Well)


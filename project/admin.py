from django.contrib import admin
from . models import Project, ProjectManager, Well, Tool, Location, Crew, Note

admin.site.register(Project)
admin.site.register(ProjectManager)
admin.site.register(Well)
admin.site.register(Tool)
admin.site.register(Location)
admin.site.register(Crew)
admin.site.register(Note)



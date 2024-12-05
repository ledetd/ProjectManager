from django.contrib import admin
from . models import Project, ProjectManager, Well, Tool, Location, Crew, Note, Day, Category, Spare, SpareLocation, Schedule, Tracker, Herc, DailyReport, Invoice

admin.site.register(Project)
admin.site.register(ProjectManager)
admin.site.register(Well)
admin.site.register(Tool)
admin.site.register(Location)
admin.site.register(Crew)
admin.site.register(Note)
admin.site.register(Day)
admin.site.register(Category)
admin.site.register(Spare)
admin.site.register(SpareLocation)
admin.site.register(Schedule)
admin.site.register(Tracker)
admin.site.register(Herc)
admin.site.register(DailyReport)
admin.site.register(Invoice)




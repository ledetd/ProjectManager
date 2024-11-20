from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=500)
    project_manager = models.ForeignKey("ProjectManager", on_delete=models.SET_NULL, null=True)
    project_location = models.CharField(max_length=500)

    def __str__(self):
        return self.project_name

class ProjectManager(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Well(models.Model):
    well_name = models.CharField(max_length=500)
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True)
    job_number = models.CharField(max_length=500)
    well_name = models.CharField(max_length=500)

    def __str__(self):
        return self.well_name
    
class Tool(models.Model):
    tool_name = models.CharField(max_length=500)
    tool_location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    well_name = models.ForeignKey("Well", on_delete=models.SET_NULL, null=True)
    tool_number = models.CharField(max_length=500)
    tool_used = models.BooleanField(default=False, null=True)
    tool_hours = models.FloatField(blank=True, null=True)
    tool_distance = models.FloatField(blank=True, null=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.tool_name} {self.tool_number}'

class Location(models.Model):
    location_name = models.CharField(max_length=500)

    def __str__(self):
        return self.location_name
    
class Crew(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    job_title = models.CharField(max_length=500)
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    airport = models.CharField(max_length=500)
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True)
    date_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
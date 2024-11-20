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
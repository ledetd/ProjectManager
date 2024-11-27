from django.db import models
from datetime import datetime


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
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.well_name
    
class Tool(models.Model):
    tool_name = models.CharField(max_length=500)
    tool_location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    well_name = models.ForeignKey("Well", on_delete=models.SET_NULL, null=True)
    tool_number = models.CharField(max_length=500)
    tool_used = models.BooleanField(default=False)
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

    BST = models.BooleanField(default=False)
    date_bst = models.DateField()
    bst_expires = models.DateField()
    IWCF = models.BooleanField(default=False)
    date_iwcf = models.DateField()
    iwcf_expires = models.DateField()
    H2S = models.BooleanField(default=False)
    date_h2s = models.DateField()
    h2s_expires = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Note(models.Model):
    subject = models.CharField(max_length=500)
    note = models.TextField(max_length=10000)
    note_date = models.DateField(auto_now_add=True)
    note_update = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.subject} {self.note_date}'
    
class Day(models.Model):
    day = models.DateField(auto_now=False)
    well_name = models.ForeignKey("Well", on_delete=models.SET_NULL, null=True)
    lift_frame = models.IntegerField(default=0)
    mpd_manifold_building = models.IntegerField(default=0)
    rcd_housing = models.IntegerField(default=0)
    pipework = models.IntegerField(default=0)
    mpd_supervisor = models.IntegerField(default=2)
    mpd_operator  = models.IntegerField(default=2)



    def __str__(self):
        return self.day.strftime("%d %B")

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Spare(models.Model):
    category_name = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=500)
    detail = models.CharField(max_length=500)
    spare_location = models.ForeignKey("SpareLocation", on_delete=models.SET_NULL, null=True)
    quantity_in_unit = models.IntegerField(default=0)
    quantity_on_location = models.IntegerField(default=0)
    vendor = models.CharField(max_length=500, null=True, blank=True)
    notes = models.CharField(max_length=10000, null=True, blank=True)
    critical_spare = models.BooleanField(default=False)

    def __str__(self):
        return self.description
    
class SpareLocation(models.Model):
    spare_location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.spare_location_name
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
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.well_name
    
class Tool(models.Model):
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True)
    tool_name = models.CharField(max_length=500)
    tool_location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
    well_name = models.ForeignKey("Well", on_delete=models.SET_NULL, null=True)
    tool_number = models.CharField(max_length=500)
    tool_used = models.BooleanField(default=False)
    tool_hours = models.FloatField(blank=True, null=True)
    tool_revolutions = models.FloatField(blank=True, null=True)
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
    on_location = models.BooleanField(default=False)

    today = models.DateField(auto_now=True)

    BST = models.BooleanField(default=False)
    date_bst = models.DateField()
    bst_expires = models.DateField()
    IWCF = models.BooleanField(default=False)
    date_iwcf = models.DateField()
    iwcf_expires = models.DateField()
    H2S = models.BooleanField(default=False)
    date_h2s = models.DateField()
    h2s_expires = models.DateField()

    @property
    def bst_expires_soon(self):
        expires_soon =  self.today - self.bst_expires
        return expires_soon
    
    @property
    def h2s_expires_soon(self):
        expires_soon = self.h2s_expires - self.today 
        return expires_soon

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Schedule(models.Model):
    crew_member = models.ForeignKey("Crew", on_delete=models.CASCADE)
    transportation_date = models.DateField()
    
    to_location = models.ForeignKey("Location", on_delete=models.CASCADE, null=True, blank=True)
    shift = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.transportation_date} {self.crew_member}'

class Note(models.Model):
    subject = models.CharField(max_length=500)
    note = models.TextField(max_length=10000)
    day_due = models.DateField(auto_now=False)
    note_date = models.DateField(auto_now_add=True)
    note_update = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.subject} {self.note_date}'
    
class Day(models.Model):
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True)
    day = models.DateField(auto_now=False)
    well_name = models.ForeignKey("Well", on_delete=models.SET_NULL, null=True)
    current_operations = models.CharField(max_length=5000, null=True, blank=True)
    future_operations = models.CharField(max_length=5000, null=True, blank=True)
    bearing_id = models.CharField(max_length=10, null=True, blank=True)
    total_rotating_hours = models.DecimalField(max_digits=8, decimal_places=1, null=True, blank=True)
    total_distance_stripped = models.DecimalField(max_digits=8, decimal_places=1, null=True, blank=True)
    total_revolutions = models.DecimalField(max_digits=8, decimal_places=1, null=True, blank=True)
    lift_frame = models.IntegerField(default=0)
    mpd_manifold_building = models.IntegerField(default=1)
    rcd_housing = models.IntegerField(default=1)
    pipework = models.IntegerField(default=1)
    mpd_supervisor = models.IntegerField(default=2)
    mpd_operator  = models.IntegerField(default=2)
    supervisor_weather_delay = models.IntegerField(default=0)
    operator_weather_delay = models.IntegerField(default=0)


    def __str__(self):
        return self.day.strftime("%d %B")
    
    @property
    def month(self):
        month = self.day.strftime("%M")
        return month

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
    
class Tracker(models.Model):

    drilledLengthRotating = models.FloatField(default=0, null=True, blank=True)
    drilledLengthSliding = models.FloatField(default=0, null=True, blank=True)
    drilledLengthTotal = models.FloatField(default=0, null=True, blank=True)
    
class Herc(models.Model):
    crew_member = models.ForeignKey("Crew", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.crew_member
    
# CHANGED TO REVENUE - REFACTOR THIS CODE
class Invoice(models.Model):
    project_name = models.ForeignKey("Project", on_delete=models.CASCADE)
    well_name = models.ForeignKey("Well", on_delete=models.CASCADE)
    invoice_date = models.DateField(auto_now=False)
    project_management = models.DecimalField(max_digits=8, decimal_places=2)
    engineering = models.DecimalField(max_digits=8, decimal_places=2)
    personnel = models.DecimalField(max_digits=8, decimal_places=2)
    equipment = models.DecimalField(max_digits=8, decimal_places=2)
    herc = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.well_name} | {self.invoice_date}'
    
    @property
    def total(self):
        total = (self.project_management+self.engineering+self.personnel+self.equipment+self.herc)
        return total
    

# PRAS

class ProjectReadinessAssessmentSection(models.Model):
    pra_section_name = models.CharField(max_length=100)

    def __str__(self):
        return self.pra_section_name

class ProjectReadinessAssessmentCategory(models.Model):
    pra_category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.pra_category_name

class ProjectReadinessAssessment(models.Model):
    pra_section_name = models.ForeignKey(ProjectReadinessAssessmentSection, related_name='pra_section', on_delete=models.CASCADE)
    pra_category_name = models.ForeignKey(ProjectReadinessAssessmentCategory, related_name='pra_category', on_delete=models.CASCADE)
    task_decsription = models.TextField(max_length=10000)
    fin_involved = models.BooleanField(default=False)
    eng_involved = models.BooleanField(default=False)
    ops_involved = models.BooleanField(default=False)
    tec_involved = models.BooleanField(default=False)
    hse_involved = models.BooleanField(default=False)
    sal_involved = models.BooleanField(default=False)
    pnc_involved = models.BooleanField(default=False)
    sup_involved = models.BooleanField(default=False)
    tra_involved = models.BooleanField(default=False)
    qty_involved = models.BooleanField(default=False)
    log_involved = models.BooleanField(default=False)
    fac_involved = models.BooleanField(default=False)
    man_involved = models.BooleanField(default=False)
    task_started = models.BooleanField(default=False)
    low_priority = models.BooleanField(default=True)
    due_date = models.DateField(auto_now=False)
    assigned_to = models.CharField(max_length=100)
    date_updated = models.DateField(auto_now_add=True)
    comments = models.TextField(max_length=100000)

    def __str__(self):
        return f'{self.pra_section_name} {self.pra_category_name}'


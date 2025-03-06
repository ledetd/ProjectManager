from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from . models import  Project, ProjectManager, Action


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(forms.ModelForm):
	projects = forms.ModelChoiceField(queryset=Project.objects.all(), initial=0),

	class Meta:
		model = Project
		fields = [ 'project_name', 'project_manager', 'project_location']

class ProjectManagerForm(forms.ModelForm):
	managers = forms.ModelChoiceField(queryset=ProjectManager.objects.all(), initial=0),

	class Meta:
		model = ProjectManager
		fields = [ 'first_name', 'last_name']

class ProjectActionForm(forms.ModelForm):
	actions = forms.ModelChoiceField(queryset=Action.objects.all(), initial=0),

	class Meta:
		model = Action
		fields = [ 'action_description']
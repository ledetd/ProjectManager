from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from . models import Note, Day, Tool, Crew, Well

class NoteForm(forms.ModelForm):
	notes = forms.ModelChoiceField(queryset=Note.objects.all(), initial=0),

	class Meta:
		model = Note
		fields = ['subject', 'note', 'completed']


class DateInput(forms.DateInput):
    input_type = 'date'

class DayForm(forms.ModelForm):
	days = forms.ModelChoiceField(queryset=Day.objects.all(), initial=0),

	class Meta:
		model = Day
		fields = [ 'day', 'well_name', 'lift_frame', 'mpd_manifold_building', 'rcd_housing', 'pipework', 'mpd_supervisor', 'mpd_operator']
		widgets = {
            'day': DateInput(),
        }

class ToolForm(forms.ModelForm):
	tools = forms.ModelChoiceField(queryset=Tool.objects.all(), initial=0),

	class Meta:
		model = Tool
		fields = ['tool_name', 'tool_location', 'well_name', 'tool_number', 'tool_used', 'tool_hours', 'tool_distance']

class CrewForm(forms.ModelForm):
	crews = forms.ModelChoiceField(queryset=Crew.objects.all(), initial=0),

	class Meta:
		model = Crew
		fields = ['first_name', 'last_name', 'job_title', 'location', 'airport', 'project', 'BST', 'IWCF']

class WellForm(forms.ModelForm):
	wells = forms.ModelChoiceField(queryset=Well.objects.all(), initial=0),

	class Meta:
		model = Well
		fields = ['well_name', 'project', 'job_number', 'active']
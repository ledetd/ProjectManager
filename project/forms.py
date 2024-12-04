from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from . models import Note, Day, Tool, Crew, Well, Spare, Tracker, Project, DailyReport

class NoteForm(forms.ModelForm):
	notes = forms.ModelChoiceField(queryset=Note.objects.all(), initial=0),

	class Meta:
		model = Note
		fields = ['subject', 'note', 'completed']


class DateInput(forms.DateInput):
    input_type = 'date'

class ProjectForm(forms.ModelForm):
	projects = forms.ModelChoiceField(queryset=Project.objects.all(), initial=0),

	class Meta:
		model = Project
		fields = [ 'project_name', 'project_manager', 'project_location']


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

class SpareForm(forms.ModelForm):
	spares = forms.ModelChoiceField(queryset=Spare.objects.all(), initial=0),

	class Meta:
		model = Spare
		fields = ['category_name', 'description', 'detail', 'spare_location', 'quantity_in_unit', 'quantity_on_location', 'vendor','notes','critical_spare']

class CrewForm(forms.ModelForm):
	crews = forms.ModelChoiceField(queryset=Crew.objects.all(), initial=0),

	class Meta:
		model = Crew
		fields = ['first_name', 'last_name', 'job_title', 'location', 'on_location', 'airport', 'project',
			 'BST', 'date_bst', 'bst_expires',  'IWCF',  'date_iwcf','iwcf_expires', 'H2S', 'date_h2s', 'h2s_expires']

		widgets = {
            'date_bst': DateInput(),
			'date_iwcf': DateInput(),
			'date_h2s': DateInput(),
			'bst_expires': DateInput(),
			'iwcf_expires': DateInput(),
			'h2s_expires': DateInput(),
        }
class WellForm(forms.ModelForm):
	wells = forms.ModelChoiceField(queryset=Well.objects.all(), initial=0),

	class Meta:
		model = Well
		fields = ['well_name', 'project', 'job_number', 'active']

class TrackerForm(forms.ModelForm):
	spares = forms.ModelChoiceField(queryset=Tracker.objects.all(), initial=0),

	class Meta:
		model = Tracker
		fields = ['project_name', 'well_name', 'hole_section', 'run_number', 'rcd_number', 'bearing_number', 'sealing_element',
			 'total_installed_time', 'total_rotating_time', 'max_rpm', 'total_stripped_length',
			   'max_connection_surface_back_pressure', 'max_drilling_surface_back_pressure', 'max_stripping_surface_back_pressure',
				 'average_flow_line_temp', 'max_flow_line_temp', 'mud_system', 'mud_weight', 'sealing_element_failure']
		
class DailyForm(forms.ModelForm):
	dailys = forms.ModelChoiceField(queryset=DailyReport.objects.all(), initial=0),

	class Meta:
		model = DailyReport
		fields = [ 'project_name', 'well_name', 'date', 'hole_diameter', 'hole_depth', 'bearing_number', 'total_length_stripped', 'total_rotating_hours']
		widgets = {
            'date': DateInput(),
        }
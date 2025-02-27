from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from . models import Note, Day, Tool, Crew, Well, Spare, Tracker, Project, Invoice


class DateInput(forms.DateInput):
    input_type = 'date'


class NoteForm(forms.ModelForm):
	notes = forms.ModelChoiceField(queryset=Note.objects.all(), initial=0),

	class Meta:
		model = Note
		fields = ['subject', 'note', 'day_due', 'completed']
		widgets = {
			'day_due': DateInput(),
		}


class ProjectForm(forms.ModelForm):
	projects = forms.ModelChoiceField(queryset=Project.objects.all(), initial=0),

	class Meta:
		model = Project
		fields = [ 'project_name', 'project_manager', 'project_location']


class DayForm(forms.ModelForm):
	days = forms.ModelChoiceField(queryset=Day.objects.all(), initial=0),

	class Meta:
		model = Day
		fields = [ 'day', 'project', 'well_name', 'current_operations', 'future_operations', 'bearing_id', 'total_rotating_hours', 'total_distance_stripped', 'total_revolutions',
			 'lift_frame', 'mpd_manifold_building', 'rcd_housing', 'pipework', 'mpd_supervisor', 'mpd_operator', 'supervisor_weather_delay', 'operator_weather_delay']
		widgets = {
            'day': DateInput(),
        }

class ToolForm(forms.ModelForm):
	tools = forms.ModelChoiceField(queryset=Tool.objects.all(), initial=0),

	class Meta:
		model = Tool
		fields = ['tool_name', 'tool_location', 'well_name', 'tool_number', 'tool_used', 'tool_in_use', 'tool_hours', 'tool_distance', 'tool_revolutions']

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
		fields = []
		

class InvoiceForm(forms.ModelForm):
	invoices = forms.ModelChoiceField(queryset=Invoice.objects.all(), initial=0),

	class Meta:
		model = Invoice
		fields = [ 'project_name', 'well_name', 'invoice_date', 'project_management', 'engineering', 'personnel', 'equipment', 'herc']
		widgets = {
            'invoice_date': DateInput(),
        }
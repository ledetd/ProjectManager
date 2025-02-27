from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, CreateView, UpdateView, DetailView, DeleteView
from . models import Project, Well, Tool, Crew, Note, Day, Spare, Tracker, Herc, Invoice
from .forms import NoteForm, DayForm, ToolForm, CrewForm, WellForm, SpareForm, TrackerForm, ProjectForm, InvoiceForm
from django.utils import timezone
from django.db.models import Sum


class Index(TemplateView):
	template_name = 'project/index.html'

class Dashboard(TemplateView):
	model = Project
	template_name = 'project/dashboard.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['projects'] = Project.objects.all()
		context['wells'] = Well.objects.all()
		context['crews'] = Crew.objects.all()
		context['tools'] = Tool.objects.all()
		context['days'] = Day.objects.all()
		context['invoices'] = Invoice.objects.all()
		
		return context
	
class ProjectDetailView( DetailView):
	model = Project
	template_name = 'project/project_detail.html'

class AddProject( CreateView):
	model = Project
	form_class = ProjectForm
	template_name = 'project/project_form.html'
	success_url = reverse_lazy('dashboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['projects'] = Project.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
	
class Crewboard(  View):
	def get(self, request):
		crews = Crew.objects.all().order_by('project', "-on_location", "-job_title",  "-location")
		return render(request, 'crew/crewboard.html', {'crews' : crews})
	
class CrewDetailView( DetailView):
	model = Crew
	template_name = 'crew/crew_detail.html'

class AddCrew( CreateView):
	model = Crew
	form_class = CrewForm
	template_name = 'crew/crew_form.html'
	success_url = reverse_lazy('crewboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['crews'] = Crew.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditCrew( UpdateView):
	model = Crew
	form_class = CrewForm
	template_name = 'crew/crew_form.html'
	success_url = reverse_lazy('crewboard')

class Wellboard(  View):
	def get(self, request):
		wells = Well.objects.all().order_by('-active','project')
		return render(request, 'wells/wellboard.html', {'wells': wells})

class WellDetailView( DetailView):
	model = Well
	template_name = 'wells/well_detail.html'

class AddWell( CreateView):
	model = Well
	form_class = WellForm
	template_name = 'wells/well_form.html'
	success_url = reverse_lazy('wellboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['wells'] = Well.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditWell( UpdateView):
	model = Well
	form_class = WellForm
	template_name = 'wells/well_form.html'
	success_url = reverse_lazy('wellboard')
	
class Scheduleboard( View):
	def get(self, request):
		return render(request, 'schedule/scheduleboard.html', {})

class Toolboard( View):
	def get(self, request):
		tools = Tool.objects.all().order_by('-tool_in_use', 'project', 'tool_used', 'tool_name','-tool_location', 'tool_number')
		return render(request, 'tools/toolboard.html', {'tools': tools})

class AddTool( CreateView):
	model = Tool
	form_class = ToolForm
	template_name = 'tools/tool_form.html'
	success_url = reverse_lazy('toolboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tools'] = Tool.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditTool( UpdateView):
	model = Tool
	form_class = ToolForm
	template_name = 'tools/tool_form.html'
	success_url = reverse_lazy('toolboard')

class Spareboard( View):
	def get(self, request):
		spares = Spare.objects.all().order_by('-spare_location')
		return render(request, 'spares/spareboard.html', {'spares': spares})

class SpareDetailView( DetailView):
	model = Spare
	template_name = 'spares/spare_detail.html'

class AddSpare( CreateView):
	model = Spare
	form_class = SpareForm
	template_name = 'spares/spare_form.html'
	success_url = reverse_lazy('spareboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['spares'] = Spare.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditSpare( UpdateView):
	model = Spare
	form_class = SpareForm
	template_name = 'spares/spare_form.html'
	success_url = reverse_lazy('spareboard')

class Noteboard( View):
	def get(self, request):
		notes = Note.objects.all(). order_by('completed','-note_date')
		return render(request, 'notes/noteboard.html', {'notes': notes})
	
class AddNote( CreateView):
	model = Note
	form_class = NoteForm
	template_name = 'notes/note_form.html'
	success_url = reverse_lazy('noteboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['notes'] = Note.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditNote( UpdateView):
	model = Note
	form_class = NoteForm
	template_name = 'notes/note_form.html'
	success_url = reverse_lazy('noteboard')

class DeleteNote( DeleteView):
	model = Note
	template_name = 'notes/delete_note.html'
	success_url = reverse_lazy('noteboard')
	context_object_name = 'note'

class Dayboard( View):
	def get(self, request):
		days = Day.objects.all().order_by('day')
		lift_sum = Day.objects.aggregate(total_lift_frame=Sum('lift_frame'))['total_lift_frame'] or 0
		mmb_sum = Day.objects.aggregate(total_mmb=Sum('mpd_manifold_building'))['total_mmb'] or 0
		rcd_sum = Day.objects.aggregate(total_rcd=Sum('rcd_housing'))['total_rcd'] or 0
		pipework_sum = Day.objects.aggregate(total_pipework=Sum('pipework'))['total_pipework'] or 0
		mmb_sum = Day.objects.aggregate(total_mmb=Sum('mpd_manifold_building'))['total_mmb'] or 0
		mpd_supervisor_sum = Day.objects.aggregate(total_mpd_supervisor=Sum('mpd_supervisor'))['total_mpd_supervisor'] or 0
		mpd_operator_sum = Day.objects.aggregate(total_mpd_operator=Sum('mpd_operator'))['total_mpd_operator'] or 0

		supervisor_weather_delay_sum = Day.objects.aggregate(total_supervisor_weather_delay=Sum('supervisor_weather_delay'))['total_supervisor_weather_delay'] or 0
		operator_weather_delay_sum = Day.objects.aggregate(total_operator_weather_delay=Sum('operator_weather_delay'))['total_operator_weather_delay'] or 0

		return render(request, 'days/dayboard.html', {'days': days, 'lift_sum': lift_sum, 'mmb_sum': mmb_sum, 'rcd_sum': rcd_sum, 'pipework_sum': pipework_sum, 'mpd_supervisor_sum': mpd_supervisor_sum, 'mpd_operator_sum': mpd_operator_sum, 'supervisor_weather_delay_sum': supervisor_weather_delay_sum, 'operator_weather_delay_sum': operator_weather_delay_sum})

class AddDay( CreateView):
	model = Day
	form_class = DayForm
	template_name = 'days/day_form.html'
	success_url = reverse_lazy('dayboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['days'] = Day.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditDay( UpdateView):
	model = Day
	form_class = DayForm
	template_name = 'days/day_form.html'
	success_url = reverse_lazy('dayboard')

class Trackerboard( View):
	def get(self, request):
		trackers = Tracker.objects.all()
		return render(request, 'tracker/trackerboard.html', {'trackers': trackers})

class TrackerDetailView( DetailView):
	model = Tracker
	template_name = 'tracker/tracker_detail.html'

class EditTracker( UpdateView):
	model = Tracker
	form_class = TrackerForm
	template_name = 'tracker/tracker_form.html'
	success_url = reverse_lazy('trackerboard')

class AddTracker( CreateView):
	model = Tracker
	form_class = TrackerForm
	template_name = 'tracker/tracker_form.html'
	success_url = reverse_lazy('trackerboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['trackers'] = Tracker.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
class Hercboard( View):
	def get(self, request):
		hercs = Herc.objects.all()
		return render(request, 'herc/hercboard.html', {'hercs': hercs})
	
# CHANGED TO REVENUE - REFACTOR THIS CODE
class Invoiceboard( View):
	def get(self, request):
		invoices = Invoice.objects.all(). order_by('project_name', 'invoice_date')

		pm_sum = Invoice.objects.aggregate(total_project_management=Sum('project_management'))['total_project_management'] or 0
		engineering_sum = Invoice.objects.aggregate(total_engineering=Sum('engineering'))['total_engineering'] or 0
		personnel_sum = Invoice.objects.aggregate(total_personnel=Sum('personnel'))['total_personnel'] or 0
		equipment_sum = Invoice.objects.aggregate(total_equipment=Sum('equipment'))['total_equipment'] or 0
		herc_sum = Invoice.objects.aggregate(total_herc=Sum('herc'))['total_herc'] or 0

		return render(request, 'invoice/invoiceboard.html', {'invoices': invoices, 'pm_sum': pm_sum, 'engineering_sum': engineering_sum, 'personnel_sum': personnel_sum, 'equipment_sum': equipment_sum, 'herc_sum': herc_sum})
	
class AddInvoice( CreateView):
	model = Invoice
	form_class = InvoiceForm
	template_name = 'invoice/invoice_form.html'
	success_url = reverse_lazy('invoiceboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['invoices'] = Invoice.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
class EditInvoice( UpdateView):
	model = Invoice
	form_class = InvoiceForm
	template_name = 'invoice/invoice_form.html'
	success_url = reverse_lazy('invoiceboard')
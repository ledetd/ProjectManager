from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, CreateView, UpdateView, DetailView, DeleteView
from . models import Project, Well, Tool, Crew, Note, Day, Spare, Tracker, Herc, DailyReport, Invoice
from .forms import NoteForm, DayForm, ToolForm, CrewForm, WellForm, SpareForm, TrackerForm, ProjectForm, DailyForm, InvoiceForm
from django.utils import timezone
from django.db.models import Sum


class Index(TemplateView):
	template_name = 'project/index.html'

class Dashboard(LoginRequiredMixin, View):
	def get(self, request):
		projects = Project.objects.all()
		return render(request, 'project/dashboard.html', {'projects': projects})
	

class AddProject(LoginRequiredMixin, CreateView):
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
	
	
class Crewboard( LoginRequiredMixin, View):
	def get(self, request):
		crews = Crew.objects.all().order_by('project', "-on_location", "-job_title", "location")
		return render(request, 'crew/crewboard.html', {'crews' : crews})
	
class CrewDetailView(LoginRequiredMixin, DetailView):
	model = Crew
	template_name = 'crew/crew_detail.html'

class AddCrew(LoginRequiredMixin, CreateView):
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

class EditCrew(LoginRequiredMixin, UpdateView):
	model = Crew
	form_class = CrewForm
	template_name = 'crew/crew_form.html'
	success_url = reverse_lazy('crewboard')

class Wellboard( LoginRequiredMixin, View):
	def get(self, request):
		wells = Well.objects.all().order_by('project','-active')
		return render(request, 'wells/wellboard.html', {'wells': wells})

class WellDetailView(LoginRequiredMixin, DetailView):
	model = Well
	template_name = 'wells/well_detail.html'

class AddWell(LoginRequiredMixin, CreateView):
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

class EditWell(LoginRequiredMixin, UpdateView):
	model = Well
	form_class = WellForm
	template_name = 'wells/well_form.html'
	success_url = reverse_lazy('wellboard')
	
class Scheduleboard(LoginRequiredMixin, View):
	def get(self, request):
		return render(request, 'schedule/scheduleboard.html', {})

class Toolboard(LoginRequiredMixin, View):
	def get(self, request):
		tools = Tool.objects.all().order_by( 'tool_name','-tool_location', 'tool_number')
		return render(request, 'tools/toolboard.html', {'tools': tools})

class AddTool(LoginRequiredMixin, CreateView):
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

class EditTool(LoginRequiredMixin, UpdateView):
	model = Tool
	form_class = ToolForm
	template_name = 'tools/tool_form.html'
	success_url = reverse_lazy('toolboard')

class Spareboard(LoginRequiredMixin, View):
	def get(self, request):
		spares = Spare.objects.all().order_by('-spare_location')
		return render(request, 'spares/spareboard.html', {'spares': spares})

class SpareDetailView(LoginRequiredMixin, DetailView):
	model = Spare
	template_name = 'spares/spare_detail.html'

class AddSpare(LoginRequiredMixin, CreateView):
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

class EditSpare(LoginRequiredMixin, UpdateView):
	model = Spare
	form_class = SpareForm
	template_name = 'spares/spare_form.html'
	success_url = reverse_lazy('spareboard')

class Noteboard(LoginRequiredMixin, View):
	def get(self, request):
		notes = Note.objects.all(). order_by('completed','-note_date')
		return render(request, 'notes/noteboard.html', {'notes': notes})
	
class AddNote(LoginRequiredMixin, CreateView):
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

class EditNote(LoginRequiredMixin, UpdateView):
	model = Note
	form_class = NoteForm
	template_name = 'notes/note_form.html'
	success_url = reverse_lazy('noteboard')

class DeleteNote(LoginRequiredMixin, DeleteView):
	model = Note
	template_name = 'notes/delete_note.html'
	success_url = reverse_lazy('noteboard')
	context_object_name = 'note'

class Dayboard(LoginRequiredMixin, View):
	def get(self, request):
		days = Day.objects.all().order_by('day')
		lift_sum = Day.objects.aggregate(total_lift_frame=Sum('lift_frame'))['total_lift_frame'] or 0
		mmb_sum = Day.objects.aggregate(total_mmb=Sum('mpd_manifold_building'))['total_mmb'] or 0
		rcd_sum = Day.objects.aggregate(total_rcd=Sum('rcd_housing'))['total_rcd'] or 0
		pipework_sum = Day.objects.aggregate(total_pipework=Sum('pipework'))['total_pipework'] or 0
		mmb_sum = Day.objects.aggregate(total_mmb=Sum('mpd_manifold_building'))['total_mmb'] or 0
		mpd_supervisor_sum = Day.objects.aggregate(total_mpd_supervisor=Sum('mpd_supervisor'))['total_mpd_supervisor'] or 0
		mpd_operator_sum = Day.objects.aggregate(total_mpd_operator=Sum('mpd_operator'))['total_mpd_operator'] or 0

		return render(request, 'days/dayboard.html', {'days': days, 'lift_sum': lift_sum, 'mmb_sum': mmb_sum, 'rcd_sum': rcd_sum, 'pipework_sum': pipework_sum, 'mpd_supervisor_sum': mpd_supervisor_sum, 'mpd_operator_sum': mpd_operator_sum })

class AddDay(LoginRequiredMixin, CreateView):
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

class EditDay(LoginRequiredMixin, UpdateView):
	model = Day
	form_class = DayForm
	template_name = 'days/day_form.html'
	success_url = reverse_lazy('dayboard')

class Trackerboard(LoginRequiredMixin, View):
	def get(self, request):
		trackers = Tracker.objects.all().order_by('well_name', '-hole_section')
		return render(request, 'tracker/trackerboard.html', {'trackers': trackers})

class TrackerDetailView(LoginRequiredMixin, DetailView):
	model = Tracker
	template_name = 'tracker/tracker_detail.html'

class EditTracker(LoginRequiredMixin, UpdateView):
	model = Tracker
	form_class = TrackerForm
	template_name = 'tracker/tracker_form.html'
	success_url = reverse_lazy('trackerboard')

class AddTracker(LoginRequiredMixin, CreateView):
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
	
class Hercboard(LoginRequiredMixin, View):
	def get(self, request):
		hercs = Herc.objects.all()
		return render(request, 'herc/hercboard.html', {'hercs': hercs})
	
class DailyReportBoard(LoginRequiredMixin, View):
	def get(self, request):
		reports = DailyReport.objects.all().order_by('date')
		return render(request, 'daily/dailyboard.html', {'reports': reports})
	
class AddDailyReport(LoginRequiredMixin, CreateView):
	model = DailyReport
	form_class = DailyForm
	template_name = 'daily/daily_form.html'
	success_url = reverse_lazy('dailyboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['reports'] = DailyReport.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
class Invoiceboard(LoginRequiredMixin, View):
	def get(self, request):
		invoices = Invoice.objects.all()
		return render(request, 'invoice/invoiceboard.html', {'invoices': invoices})
	
class AddInvoice(LoginRequiredMixin, CreateView):
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
	
class EditInvoice(LoginRequiredMixin, UpdateView):
	model = Invoice
	form_class = InvoiceForm
	template_name = 'invoice/invoice_form.html'
	success_url = reverse_lazy('invoiceboard')
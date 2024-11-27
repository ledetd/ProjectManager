from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, CreateView, UpdateView, DetailView, DeleteView
from . models import Project, Well, Tool, Crew, Note, Day, Spare
from .forms import NoteForm, DayForm, ToolForm, CrewForm, WellForm, SpareForm
from django.utils import timezone



class Index(TemplateView):
	template_name = 'project/index.html'

class Dashboard(LoginRequiredMixin, View):
	def get(self, request):
		projects = Project.objects.all()
		return render(request, 'project/dashboard.html', {'projects': projects})
	
class Crewboard( LoginRequiredMixin, View):
	def get(self, request):
		crews = Crew.objects.all().order_by( '-BST', 'location','job_title')
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
		wells = Well.objects.all().order_by('-active')
		return render(request, 'wells/wellboard.html', {'wells': wells})

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
		spares = Spare.objects.all()
		return render(request, 'spares/spareboard.html', {'spares': spares})

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

	
class Dayboard(LoginRequiredMixin, View):
	def get(self, request):
		days = Day.objects.all().order_by('day')
		return render(request, 'days/dayboard.html', {'days': days})
	
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









from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from . models import Project, Well, Tool, Crew, Note, Day
from .forms import NoteForm, DayForm

class Index(TemplateView):
	template_name = 'project/index.html'

class Dashboard( View):
	def get(self, request):
		projects = Project.objects.all()
		return render(request, 'project/dashboard.html', {'projects': projects})
	
class Crewboard( View):
	def get(self, request):
		crews = Crew.objects.all().order_by('location','job_title')
		return render(request, 'crew/crewboard.html', {'crews' : crews})
	
class Wellboard( View):
	def get(self, request):
		wells = Well.objects.all()
		return render(request, 'wells/wellboard.html', {'wells': wells})
	
class Scheduleboard( View):
	def get(self, request):
		return render(request, 'schedule/scheduleboard.html', {})

class Toolboard( View):
	def get(self, request):
		tools = Tool.objects.all().order_by('-tool_location', 'tool_number')
		return render(request, 'tools/toolboard.html', {'tools': tools})
	
class Noteboard( View):
	def get(self, request):
		notes = Note.objects.all(). order_by('-note_date')
		return render(request, 'notes/noteboard.html', {'notes': notes})
	
class AddNote(CreateView):
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

class EditNote(UpdateView):
	model = Note
	form_class = NoteForm
	template_name = 'notes/note_form.html'
	success_url = reverse_lazy('noteboard')


	
class Dayboard( View):
	def get(self, request):
		days = Day.objects.all().order_by('day')
		return render(request, 'days/dayboard.html', {'days': days})
	
class AddDay(CreateView):
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

class EditDay(UpdateView):
	model = Day
	form_class = DayForm
	template_name = 'days/day_form.html'
	success_url = reverse_lazy('dayboard')
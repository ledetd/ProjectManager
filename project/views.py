from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from . models import Project, Well, Tool, Crew, Note


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
		notes = Note.objects.all()
		return render(request, 'notes/noteboard.html', {'notes': notes})
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from . models import Project, Well, ProjectManager



class Index(TemplateView):
	template_name = 'project/index.html'

class Dashboard( View):
	def get(self, request):
		projects = Project.objects.all()
		return render(request, 'project/dashboard.html', {'projects': projects})
	
class Crewboard( View):
	def get(self, request):
		return render(request, 'crew/crewboard.html', {})
	
class Wellboard( View):
	def get(self, request):
		wells = Well.objects.all()
		return render(request, 'wells/wellboard.html', {'wells': wells})
	
class Scheduleboard( View):
	def get(self, request):
		return render(request, 'schedule/scheduleboard.html', {})


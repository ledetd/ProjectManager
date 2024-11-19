from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView



class Index(TemplateView):
	template_name = 'project/index.html'

class Dashboard( View):
	def get(self, request):
		return render(request, 'project/dashboard.html', {})
	
class Crewboard( View):
	def get(self, request):
		return render(request, 'crew/crewboard.html', {})
	
class Wellboard( View):
	def get(self, request):
		return render(request, 'wells/wellboard.html', {})


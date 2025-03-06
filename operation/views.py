from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from . models import Project, ProjectManager, Action
from . forms import ProjectForm, ProjectManagerForm, ProjectActionForm


class Home(TemplateView):
	template_name = 'operation/home.html'

class Dashboard(TemplateView):
	model = Project
	template_name = 'operation/dashboard.html'

class AddProject(CreateView):
	model = Project
	form_class = ProjectForm
	template_name = 'operation/project_form.html'
	success_url = reverse_lazy('ooperation-dashboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['projects'] = Project.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class AddManager(CreateView):
	model = ProjectManager
	form_class = ProjectManagerForm
	template_name = 'operation/project_manager_form.html'
	success_url = reverse_lazy('operation-dashboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['managers'] = ProjectManager.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class AddAction(CreateView):
	model = Action
	form_class = ProjectActionForm
	template_name = 'operation/project_action_form.html'
	success_url = reverse_lazy('operation-dashboard')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['actions'] = Action.objects.all()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	
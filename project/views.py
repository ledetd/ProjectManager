from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(TemplateView):
	template_name = 'project/index.html'

class Dashboard(LoginRequiredMixin, View):
	def get(self, request):


		return render(request, 'project/dashboard.html', {})


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.utils import timezone
from django.db.models import Sum


class Home(TemplateView):
	template_name = 'projectreadiness/home.html'
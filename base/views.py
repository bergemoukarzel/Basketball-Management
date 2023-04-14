from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

class PlayerList(ListView):
    model = Task
    context_object_name = 'Players'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'player'
    template_name = 'base/player.html'

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy
from .models import Task

class PlayerList(ListView):
    model = Task
    context_object_name = 'players'

class PlayerDetail(DetailView):
    model = Task
    context_object_name = 'player'
    template_name = 'base/player.html'

class PlayerCreate(CreateView):
    model = Task
    #field = ['title', 'description']
    fields = '__all__'
    success_url = reverse_lazy('players')
    template_name = 'base/Player_form.html'
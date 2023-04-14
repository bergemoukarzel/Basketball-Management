from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
      return reverse_lazy('BasketballPlayers')


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
    success_url = reverse_lazy('BasketballPlayers')
    #or players
    template_name = 'base/Player_form.html'

class PlayerUpdate(UpdateView):
    model = Task
    fields ='__all__'
    success_url = reverse_lazy('BasketballPlayers')
    template_name = 'base/Player_form.html'

class PlayerDelete(DeleteView):
    model = Task
    context_object_name = 'player'
    template_name = 'base/player_confirm_delete.html'
    success_url = reverse_lazy('BasketballPlayers')

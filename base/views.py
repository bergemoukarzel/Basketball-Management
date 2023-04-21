from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
      return reverse_lazy('BasketballPlayers')


class RegisterPage(FormView):
    template_name='base/register.html'
    form_class= UserCreationForm
    redirect_authenticated_user= True
    success_url = reverse_lazy('BasketballPlayers')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('BasketballPlayers')
        return super(RegisterPage, self).get(*args, **kwargs)

class PlayerList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'players'
    template_name = 'base/Player_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = context['players'].filter(user=self.request.user)
        search_input = self.request.GET.get('search-area', '')
        if search_input:
            context['players'] = context['players'].filter(title__icontains=search_input)

        context['search_input'] = search_input
        return context

class PlayerDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'player'
    template_name = 'base/player.html'

class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('BasketballPlayers')
    template_name = 'base/Player_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerCreate, self).form_valid(form)

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description']
    success_url = reverse_lazy('BasketballPlayers')
    template_name = 'base/Player_form.html'

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'player'
    template_name = 'base/player_confirm_delete.html'
    success_url = reverse_lazy('BasketballPlayers')

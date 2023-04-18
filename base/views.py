from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Game,Team,Admin,User,Player,Coach
from .forms import addNewGame, createNewTeam
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(response):
    if response.user.is_authenticated and hasattr(response.user,"admin"):
        return  HttpResponseRedirect("/ad/home")
    if response.user.is_authenticated and hasattr(response.user,"player"):
        return  HttpResponseRedirect("/player/home")
    elif response.user.is_authenticated:
        return HttpResponseRedirect("/teams")
    else:
        return  HttpResponseRedirect("/login")
    



class AdminRequiredMixin(LoginRequiredMixin):
    model = Admin

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not self.request.user.admin:
            raise Http404
        return super().dispatch(request, *args, **kwargs)
    
class PlayerRequiredMixin(LoginRequiredMixin):
    model = Player

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not self.request.user.player:
            raise Http404
        return super().dispatch(request, *args, **kwargs)




class AdminBase(AdminRequiredMixin, TemplateView):
    template_name = "base/admin.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user.username
        return context


class AdminHome(AdminRequiredMixin, TemplateView):
    template_name="base/admin-home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user.username
        return context
    
class AdminRoster(AdminRequiredMixin, TemplateView):
    template_name="base/admin-roster.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["players"] = self.request.user.admin.team.player_set.all
        context["coach"] = self.request.user.admin.team.coach_set.all
        context["user"] = self.request.user.username
        search_input = self.request.GET.get('search-area', '')
        if search_input:
            context['players'] = self.request.user.admin.team.player_set.filter(name__icontains=search_input)

        context['search_input'] = search_input

        search_in = self.request.GET.get('search', '')
        if search_in:
            context['coach'] = self.request.user.admin.team.coach_set.filter(name__icontains=search_in)

        context['search_in'] = search_in

        return context


class adminPlayerCreate(AdminRequiredMixin, CreateView):
    model = Player
    fields = ['name','user','stats']
    success_url = reverse_lazy('rosterAdmin')
    template_name = 'base/admin-player-create.html'

    def form_valid(self, form):
        form.instance.team = self.request.user.admin.team
        return super(adminPlayerCreate, self).form_valid(form)
    
class adminCoachCreate(AdminRequiredMixin, CreateView):
    model = Coach
    fields = ['name','user']
    success_url = reverse_lazy('rosterAdmin')
    template_name = 'base/admin-coach-create.html'

    def form_valid(self, form):
        form.instance.team = self.request.user.admin.team
        return super(adminCoachCreate, self).form_valid(form)
    
class adminPlayerUpdate(AdminRequiredMixin, UpdateView):
    model = Player
    fields = ['name','user','stats']
    success_url = reverse_lazy('rosterAdmin')
    template_name = 'base/admin-player-update.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team"] = self.request.user.admin.team
        context["player"] = self.object
        return context
    
class AdminPlayerDetail(AdminRequiredMixin, DetailView):
    model = Player
    context_object_name = 'player'
    template_name = 'base/admin-player-detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team"] = self.request.user.admin.team
        return context

class adminPlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    context_object_name = 'player'
    template_name = 'base/admin-player-delete.html'
    success_url = reverse_lazy('rosterAdmin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team"] = self.request.user.admin.team
        return context




class PlayerBase(PlayerRequiredMixin, TemplateView):
    template_name = "base/player.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user.username
        return context

class PlayerGames(PlayerRequiredMixin, TemplateView):
    template_name = "base/player-games.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user.username
        context["t"] = self.request.user.player.team
        context["d"] = self.request.user.player.team.game_set.all().order_by('date')
        return context
    
class PlayerHome(PlayerRequiredMixin, TemplateView):
    template_name = "base/player-home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user.username
        context["t"] = self.request.user.player.team
        return context
    
class PlayerRoster(PlayerRequiredMixin, TemplateView):
    template_name = "base/player-roster.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user.username
        context["t"] = self.request.user.player.team
        return context





def homeGuest(response,id):
    if response.user.is_authenticated:
        i = Team.objects.get(id=id)
        return render(response, "base/guest-home.html", {"i":i})
    else:  
        return HttpResponseRedirect("/")
    


def gamesGuest(response,id):
    if response.user.is_authenticated:
        i = Team.objects.get(id=id)
        return render(response, "base/guest-games.html", {"i":i})
    else:  
        return HttpResponseRedirect("/")
    


def createTeam(response):
    if response.method == "POST":
        form = createNewTeam(response.POST)

        if form.is_valid():
             n = form.cleaned_data["name"]
             t = Team(name = n)
             t.save()
             u = response.user
             a = Admin(user = u, team = t)
             a.save()
             return HttpResponseRedirect(f"../ad/home")
    else:
        form = createNewTeam()
    return render(response, "base/create-team.html", {"form": form} )



def teams(response):
    t = Team.objects.all()

    return render(response, "base/teams.html", {"t":t})



def games(response):
    if response.user.is_authenticated and hasattr(response.user,"admin"):
        t = response.user.admin.team
        user = response.user.username
        d = t.game_set.all().order_by('date')

        if response.method == "POST":
            if response.POST.get("save"):
                for game in t.game_set.all():
                    if response.POST.get("c" + str(game.id)) == "clicked":
                        game.complete = True
                    else:
                        game.complete = False

                    game.save()
            if response.POST.get("del"):
                for game in t.game_set.all():
                    if response.POST.get("c" + str(game.id)) == "clicked":
                        game.delete()
                    else:
                        game.complete = False      
                        game.save()              
            
            elif response.POST.get("newGame"):
                txt = response.POST.get("game")
                txtd = response.POST.get("date")

                if len(txt) >= 1:
                    t.game_set.create(team2=txt, date=txtd)

                else:
                    pass
            
            elif response.POST.get("newPractice"):
                txt = response.POST.get("pdate")
                if len(txt) >= 1:
                    t.game_set.create(date=txt,practice=True,team2="None")
                else:
                    pass
                
        return render(response, "base/admin-games.html", {"t":t, "d":d,"user":user})
    else:
        return HttpResponseRedirect("/")
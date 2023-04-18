from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("ad/roster/create", views.adminPlayerCreate.as_view(), name="createPlayerAdmin"),
    path("ad/roster/create/coach", views.adminCoachCreate.as_view(), name="createCoachAdmin"),
    path("ad/roster/update/<int:pk>", views.adminPlayerUpdate.as_view(), name="updatePlayerAdmin"),
    path("ad/roster/details/<int:pk>", views.AdminPlayerDetail.as_view(), name="detailsPlayerAdmin"),
    path("ad/roster/delete/<int:pk>", views.adminPlayerDelete.as_view(), name="deletePlayerAdmin"),
    path("ad/home", views.AdminHome.as_view(), name="homeAdmin"),
    path("ad/roster", views.AdminRoster.as_view(), name="rosterAdmin"),
    path("ad/", views.AdminBase.as_view(), name="baseAdmin"),
    path("player/games", views.PlayerGames.as_view(), name="gamesPlayer"),
    path("player/home", views.PlayerHome.as_view(), name="homePlayer"),
    path("player/roster", views.PlayerRoster.as_view(), name="rosterPlayer"),
    path("player/", views.PlayerBase.as_view(), name="basePlayer"),
    path("teams/create", views.createTeam, name="createTeam"),
    path("teams/", views.teams, name="teams"),
    path("home/<int:id>", views.homeGuest, name="homeGuest"),
    path("games/<int:id>", views.gamesGuest, name="gamesGuest"),
    path("ad/games", views.games, name="gamesAdmin"),

]
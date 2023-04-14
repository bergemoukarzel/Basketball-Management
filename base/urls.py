from django.urls import path 
from .views  import PlayerList, TaskDetail
urlpatterns = [
    path('', PlayerList.as_view(), name = 'BasketballPlayers'),
    path('player/<int:pk>/', TaskDetail.as_view(), name='player'),
]
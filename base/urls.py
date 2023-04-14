from django.urls import path 
from .views  import PlayerList, PlayerDetail, PlayerCreate
urlpatterns = [
    path('', PlayerList.as_view(), name = 'BasketballPlayers'),
    path('player/<int:pk>/', PlayerDetail.as_view(), name='player'),
    path('player-create/', PlayerCreate.as_view(), name = 'player-create'),
]
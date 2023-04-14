from django.urls import path
from .views  import PlayerList, PlayerDetail, PlayerCreate, PlayerUpdate, PlayerDelete
urlpatterns = [
    path('', PlayerList.as_view(), name = 'BasketballPlayers'),
    path('player/<int:pk>/', PlayerDetail.as_view(), name='player'),
    path('player-create/', PlayerCreate.as_view(), name = 'player-create'),
    path('player-update/<int:pk>/', PlayerUpdate.as_view(), name='player-update'),
    path('player-delete/<int:pk>/', PlayerDelete.as_view(), name='player-delete'),
]
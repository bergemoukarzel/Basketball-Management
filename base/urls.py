from django.urls import path
from .views  import PlayerList, PlayerDetail, PlayerCreate, PlayerUpdate, PlayerDelete, CustomLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name='logout'),
    path('', PlayerList.as_view(), name = 'BasketballPlayers'),
    path('player/<int:pk>/', PlayerDetail.as_view(), name='player'),
    path('player-create/', PlayerCreate.as_view(), name = 'player-create'),
    path('player-update/<int:pk>/', PlayerUpdate.as_view(), name='player-update'),
    path('player-delete/<int:pk>/', PlayerDelete.as_view(), name='player-delete'),
]
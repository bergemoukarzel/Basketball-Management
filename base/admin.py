from django.contrib import admin
from .models import Game,Team,Admin,Player,Coach

# Register your models here.
admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Admin)
admin.site.register(Player)
admin.site.register(Coach)
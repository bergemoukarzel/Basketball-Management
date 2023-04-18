from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Player(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    stats = models.TextField(null=True, blank=True)

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Game(models.Model):
    team1 = models.ForeignKey(Team, on_delete = models.CASCADE)
    team2 = models.CharField(max_length=200, default=None)
    date = models.DateTimeField()
    complete = models.BooleanField(default=False)
    practice = models.BooleanField(default=False)

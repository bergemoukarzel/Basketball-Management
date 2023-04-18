from django import forms

class addNewGame(forms.Form):
    team = forms.CharField(label = "Team Name", max_length=200)
    date = forms.DateTimeField()

class createNewTeam(forms.Form):
    name = forms.CharField(label = "Team Name", max_length=200)

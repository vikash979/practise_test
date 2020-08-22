from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
#from users.models import CustomUser
from django.conf import settings


class TeamStructure(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name =  models.CharField(max_length=200,unique=True)
    identifier =  models.CharField(max_length=200)
    club =  models.CharField(max_length=200)
    logoUri = models.FileField(upload_to='team/logo/',blank=True,null=True)
    
    def __str__(self):
        return self.name





class TeamPlayerStructure(models.Model):
	parent = models.ForeignKey(TeamStructure,null=True, related_name ="teamstructure" , blank=True, on_delete=models.SET_NULL)
	added_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	firstname =  models.CharField(max_length=200, blank=True)
	lastname =  models.CharField(max_length=200, blank=True)
	identifier =  models.CharField(max_length=200, blank=True)
	
	imageUri = models.FileField(upload_to='team/player_image/',blank=True,null=True)
	Player_jersey_number = models.IntegerField(blank=True, null=True)
	country = models.CharField(max_length=200, blank=True)


	def __str__(self):
	    return self.firstname


	@property
	def get_fullname(self):
		return self.firstname




class playerHistory(models.Model):
	team_player = models.ForeignKey(TeamPlayerStructure,null=True, related_name ="playerhistory" , blank=True, on_delete=models.SET_NULL)
	matches = models.IntegerField(blank=True, null=True)
	run = models.IntegerField(blank=True, null=True)
	highest_scores = models.IntegerField(blank=True, null=True)
	fifties = models.IntegerField(blank=True, null=True)
	hundreds = models.IntegerField(blank=True, null=True)




class Matches(models.Model):
	tournament_name = models.CharField(max_length=200)
	team1 = models.ForeignKey(TeamStructure,null=True, related_name ="club_team_a" , blank=True, on_delete=models.SET_NULL)
	team2 = models.ForeignKey(TeamStructure,null=True, related_name ="club_beam_b" , blank=True, on_delete=models.SET_NULL)
	winner_team = models.ForeignKey(TeamStructure,null=True, related_name ="teammatcheswinner" , blank=True, on_delete=models.SET_NULL)
	looser_team = models.ForeignKey(TeamStructure,null=True, related_name ="teammatchesloser" , blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.tournament_name

# class MatchesWinner(models.Model):
# 	match_winner = models.ForeignKey(Matches,null=True, related_name ="match_related" , blank=True, on_delete=models.SET_NULL)


class Tablepoint(models.Model):
	matches = models.ForeignKey(Matches,null=True, related_name ="matches" , blank=True, on_delete=models.SET_NULL)
	team_point = models.IntegerField(blank=True, null=True)








   
    
   
    
    
    
    
    
    
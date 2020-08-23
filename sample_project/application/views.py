from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from application.models import TeamStructure, playerHistory
from django.views.generic import TemplateView , View
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from . import serializers
from django.template.loader import get_template
from django.contrib.auth import authenticate,login,logout
from rest_framework import permissions
from rest_framework import authentication

from collections import deque
from itertools import islice



class TeamViews(TemplateView):
	template_name = "application/index.html"
	#@login_required_custom(login_url='/')
	def get(self, request, id=None):


		context_data = {}
		context_data['error'] = ''
		context_data['team_list'] = TeamStructure.objects.all().order_by("-id")

		

		return render(request, self.template_name, context_data)

class MenuApiView(APIView):
	permission_classes = [permissions.IsAuthenticated]
	authentication_classes = [authentication.SessionAuthentication]
    #authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]

	def get(self,request):
		

		

		if (request.GET.get('userid') != None):

			teaamId =  request.GET.get('userid')
			
			team_obj = TeamStructure.objects.filter(id=teaamId)
		else:
			
			team_obj = TeamStructure.objects.all()
		#team_obj = TeamStructure.objects.all()
			
		serializer = serializers.teamStrucureSerializer(team_obj,many=True)
		return Response(serializer.data)


class TornamentView(APIView):
	permission_classes = [permissions.IsAuthenticated]
	authentication_classes = [authentication.SessionAuthentication]

	def tournamentlist(self,teams):

		if len(teams) % 2:
			teams.append('Day off')
    		
		n = len(teams)
		roundmatchs = []
		fixtures = []
		return_matchs = []
		for fixture in range(1, n):
		    for i in range(n//2):
		        roundmatchs.append((teams[i], teams[n - 1 - i]))
		        return_matchs.append((teams[n - 1 - i], teams[i]))
		    teams.insert(1, teams.pop())
		    fixtures.insert(len(fixtures)//2, roundmatchs)
		    fixtures.append(return_matchs)
		    roundmatchs = []
		    return_matchs = []
		print("::::::::::::::",fixtures)

		teams_mate = []
		for fixture in fixtures:
			for xx in fixture:
				teams_mate.append(xx)

		##rint(list(set(teams_mate)))
		team_final = []
		import random 
		for yy in range(len(teams_mate)):
			for j in range(yy+1, len(teams_mate)):
				if set(teams_mate[yy]) ==set(teams_mate[j]):
					team_final.append(teams_mate[yy])
		return random.sample(team_final,6)


				

	
    		
        	

	    
	    
	    

	def get(self,request):
		team_tournament =  TeamStructure.objects.all().values('name')
		team_data = [team_obj['name'] for team_obj in  team_tournament]
		
		
		team_match =self.tournamentlist(team_data)
		
		return Response(team_match)


class PlayerHistoryView(APIView):
	def get(self,request):
		if (request.GET.get('userid') != None):

			teaamId =  request.GET.get('userid')
			
			playerList = playerHistory.objects.filter(team_player=teaamId)
			serializer = serializers.playerHistorySerializer(playerList, many=True)

		else:
			playerList = playerHistory.objects.all()
			serializer = serializers.playerHistorySerializer(playerList, many=True)


		return Response(serializer.data)


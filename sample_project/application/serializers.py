from rest_framework import serializers
from .models import TeamStructure, TeamPlayerStructure, Matches, playerHistory
from django.db.models import Q


class MatchesSerializer(serializers.ModelSerializer):
	# def to_representation(self,obj):
	# 	data = super(MatchesSerializer, self).to_representation(obj)

	# 	print(":::::::::::", data['winner_team'])
	# 	team_data =  TeamStructure.objects.filter(id=data['winner_team'])
	# 	print(":::::::::::::::::::::::",team_data)

	# 	return data['winner_team']

	# def to_representation(self,obj):
	# 	data = super(MatchesSerializer, self).to_representation(obj)
	# 	print("!!!!!!!!",data['looser_team'])
	# 	return data['looser_team']



	class Meta:
		model = Matches
		fields = '__all__'

class playerHistorySerializer(serializers.ModelSerializer):

	class Meta:
		model = playerHistory
		fields = '__all__'


class TeamPlayerStructureSerializer(serializers.ModelSerializer):
	playerhistory = playerHistorySerializer(many=True) 

	class Meta:
		model = TeamPlayerStructure
		fields = '__all__'

class teamStrucureSerializer(serializers.ModelSerializer):
	teamstructure = TeamPlayerStructureSerializer(many=True)
	#teammatcheswinner = MatchesSerializer(many=True)
	winner_team = serializers.SerializerMethodField()
	looser_team = serializers.SerializerMethodField()
	class Meta:
		model = TeamStructure
		fields = '__all__'

	def get_winner_team(self,obj):
		match_obj = Matches.objects.filter(winner_team=obj.id)
		#print(obj.id,"::::::::::",match_obj.values('winner_team','looser_team'))
		match_objects = {"data":MatchesSerializer(match_obj,many=True).data}
		match_objects['winner'] = Matches.objects.filter(winner_team=obj.id).count()

		return(match_objects)

	def get_looser_team(self,obj):
		match_obj = Matches.objects.filter(looser_team=obj.id)
		#print(obj.id,"::::::::::",match_obj.values('winner_team','looser_team'))
		match_lose = {"data":MatchesSerializer(match_obj,many=True).data}
		match_lose['loose'] = Matches.objects.filter(looser_team=obj.id).count()


		return(match_lose)




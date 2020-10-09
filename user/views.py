from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from .models import UserDetail, Borrower, BorrowedBy
from django.views.generic import TemplateView , View
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from . import serializers
from django.template.loader import get_template


class UserApiView(APIView):

	def get(self,request):
		queryset = UserDetail.objects.all()
		serializer = serializers.UserDetailSerializer(queryset,many=True)
		return Response(serializer.data)

	def post(self,request):
		name = request.data['name']
		user_detail = UserDetail.objects.create(name=name)
		queryset = UserDetail.objects.all()
		serializer = serializers.UserDetailSerializer(queryset,many=True)
		

		return Response(serializer.data)
class userViewset(viewsets.ModelViewSet):
	queryset = UserDetail.objects.all()
	serializer_class = serializers.UserDetailSerializer

	def create(self,request):
		name = request.data['name']
		user_detail = UserDetail.objects.create(name=name)
		queryset = UserDetail.objects.all()
		serializer = serializers.UserDetailSerializer(queryset,many=True)
		

		return Response(serializer.data)
    



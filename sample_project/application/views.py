from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from application.models import TeamStructure
from django.views.generic import TemplateView , View
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
#from . import serializers
from django.template.loader import get_template
from django.contrib.auth import authenticate,login,logout



class TeamViews(TemplateView):
	template_name = "application/index.html"
	#@login_required_custom(login_url='/')
	def get(self, request, id=None):


		context_data = {}
		context_data['error'] = ''
		context_data['team_list'] = TeamStructure.objects.all().order_by("-id")

		

		return render(request, self.template_name, context_data)

class MenuApiView(APIView):
	def get(self,request):
		return Response({"sss:dsdsd"})
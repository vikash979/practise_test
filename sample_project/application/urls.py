from django.urls import re_path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from application import views
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()

urlpatterns = [

    re_path(r'^home/$', views.TeamViews.as_view(), name="home"),
    re_path(r'^menu_detail/$', views.MenuApiView.as_view(), name="menu_detail"),
   # re_path(r'^menu_details/$', views.MenuApiView.as_view(), name="menu_details"),team_tournament
    re_path(r'^team_tournament/$', views.TornamentView.as_view(), name="team_tournament"),
    re_path(r'^player_history/$', views.PlayerHistoryView.as_view(), name="player_history")

    ]
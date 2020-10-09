from django.urls import re_path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
#router.register(r'dit', views.parentViewViewset)
#router.register(r'users', views.UserViewSet)


urlpatterns = [

    re_path(r'^user_detail/$', views.UserApiView.as_view(), name="user_detail"),
    re_path(r'^user_ob/$', views.userViewset.as_view({'get': 'list', 'post': 'create'}), name="user_ob"),
   
]
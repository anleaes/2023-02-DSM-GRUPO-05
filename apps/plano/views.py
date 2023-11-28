from django.shortcuts import render

# Create your views here.

from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'plano'

router = routers.DefaultRouter()
router.register('', views.planoViewSet, basename='plano')

urlpatterns = [
    path('', include(router.urls) )
]
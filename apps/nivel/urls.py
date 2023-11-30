from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'nivel'

router = routers.DefaultRouter()
router.register('nivel', views.nivelViewSet, basename='nivel')

urlpatterns = [
    path('', include(router.urls) )
]
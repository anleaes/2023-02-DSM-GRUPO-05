from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'treino'

router = routers.DefaultRouter()
router.register('', views.treinoViewSet, basename='treino')
router.register('', views.treinoexerciciokViewSet, basename='treinoexercicio')

urlpatterns = [
    path('', include(router.urls) )
]
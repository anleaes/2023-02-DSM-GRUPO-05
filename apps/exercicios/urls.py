from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'exercicio'

router = routers.DefaultRouter()
router.register('', views.exercicioViewSet, basename='exercicio')

urlpatterns = [
    path('', include(router.urls) )
]
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'avaliacao'

router = routers.DefaultRouter()
router.register('avaliacao', views.avaliacaoViewSet, basename='avaliacao')

urlpatterns = [
    path('', include(router.urls) )
]
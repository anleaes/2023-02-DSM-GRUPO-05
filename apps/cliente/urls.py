from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'cliente'

router = routers.DefaultRouter()
router.register('', views.clienteViewSet, basename='cliente')
router.register('', views.clientenivelViewSet, basename='cliente_nivel')
router.register('', views.clienteplanoViewSet, basename='cliente_plano')

urlpatterns = [
    path('', include(router.urls) )
]
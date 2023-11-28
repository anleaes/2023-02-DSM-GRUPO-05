from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'avaliacao_fisica'

router = routers.DefaultRouter()
router.register('avaliacao_fisica', views.CategoryViewSet, basename='avaliacao_fisica')

urlpatterns = [
    path('', include(router.urls) )
]

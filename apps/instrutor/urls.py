from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'instrutor'

router = routers.DefaultRouter()
router.register('', views.instrutorViewSet, basename='instrutor')

urlpatterns = [
    path('', include(router.urls) )
]
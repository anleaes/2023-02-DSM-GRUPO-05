from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'socialnetworks'

router = routers.DefaultRouter()
router.register('redessociais', views.SocialnetworkViewSet, basename='redessociais')

urlpatterns = [
    path('', include(router.urls) )
]
from django.shortcuts import render
from .models import Socialnetwork
from rest_framework import viewsets
from .serializer import SocialnetworkSerializer

# Create your views here.

class SocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = Socialnetwork.objects.all()
    serializer_class = SocialnetworkSerializer
from django.shortcuts import render
from .models import Client, ClientSocialnetwork
from rest_framework import viewsets
from .serializer import ClientSerializer, ClientSocialnetworkSerializer

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  

class ClientSocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = ClientSocialnetwork.objects.all()
    serializer_class = ClientSocialnetworkSerializer
from django.shortcuts import render
from .models import cliente, clientenivel, clienteplano
from rest_framework import viewsets
from .serializer import clienteSerializer, clientenivelSerializer, clienteplanoSerializer

# Create your views here.

class clienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer  

class clientenivelViewSet(viewsets.ModelViewSet):
    queryset = clientenivel.objects.all()
    serializer_class = clientenivelSerializer

class clienteplanoViewSet(viewsets.ModelViewSet):
    queryset = clienteplano.objects.all()
    serializer_class = clienteplanoSerializer
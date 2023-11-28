from django.shortcuts import render
from .models import cliente, clienteavaliacao, clienteplano
from rest_framework import viewsets
from .serializer import clienteSerializer, clienteavaliacaoSerializer, clienteplanoSerializer

# Create your views here.

class clienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer  

class clienteavaliacaoViewSet(viewsets.ModelViewSet):
    queryset = clienteavaliacao.objects.all()
    serializer_class = clienteavaliacaoSerializer

class clienteplanoViewSet(viewsets.ModelViewSet):
    queryset = clienteplano.objects.all()
    serializer_class = clienteplanoSerializer
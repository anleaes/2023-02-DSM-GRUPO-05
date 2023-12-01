from django.shortcuts import render
from .models import treino, treinoexercicio
from rest_framework import viewsets
from .serializer import treinoSerializer, treinoexercicioSerializer
# Create your views here.

class treinoViewSet(viewsets.ModelViewSet):
    queryset = treino.objects.all()
    serializer_class = treinoSerializer  

class treinoexercicioViewSet(viewsets.ModelViewSet):
    queryset = treinoexercicio.objects.all()
    serializer_class = treinoexercicioSerializer

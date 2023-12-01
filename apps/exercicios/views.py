from django.shortcuts import render
from .models import exercicio
from rest_framework import viewsets
from .serializer import exercicioSerializer

# Create your views here.

class exercicioViewSet(viewsets.ModelViewSet):
    queryset = exercicio.objects.all()
    serializer_class = exercicioSerializer  
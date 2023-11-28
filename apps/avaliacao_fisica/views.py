from django.shortcuts import render
from .models import avaliacao_fisica
from rest_framework import viewsets
from .serializer import avaliacao_fisicaSerializer

# Create your views here.

class avaliacao_fisicaViewSet(viewsets.ModelViewSet):
    queryset = avaliacao_fisica.objects.all()
    serializer_class = avaliacao_fisicaSerializer
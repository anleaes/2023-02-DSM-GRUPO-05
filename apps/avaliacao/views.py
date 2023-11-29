from django.shortcuts import render
from .models import avaliacao
from rest_framework import viewsets
from .serializer import avaliacaoSerializer

# Create your views here.

class avaliacaoViewSet(viewsets.ModelViewSet):
    queryset = avaliacao.objects.all()
    serializer_class = avaliacaoSerializer
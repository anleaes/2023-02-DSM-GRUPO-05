from django.shortcuts import render
from .models import nivel
from rest_framework import viewsets
from .serializer import nivelSerializer

# Create your views here.

class nivelViewSet(viewsets.ModelViewSet):
    queryset = nivel.objects.all()
    serializer_class = nivelSerializer
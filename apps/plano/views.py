from django.shortcuts import render
from .models import plano
from rest_framework import viewsets
from .serializer import planoSerializer

# Create your views here.

class planoViewSet(viewsets.ModelViewSet):
    queryset = plano.objects.all()
    serializer_class = planoSerializer 

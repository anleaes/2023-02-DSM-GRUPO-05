from django.shortcuts import render
from .models import instrutor
from rest_framework import viewsets
from .serializer import instrutorSerializer

# Create your views here.

class instrutorViewSet(viewsets.ModelViewSet):
    queryset = instrutor.objects.all()
    serializer_class = instrutorSerializer  

from django.shortcuts import render
from .models import agendamento, agendamentoinstrutor, agendamentocliente
from rest_framework import viewsets
from .serializer import agendamentoSerializer, agendamentoinstrutorSerializer, agendamentoclienteSerializer

# Create your views here.

class agendamentoViewSet(viewsets.ModelViewSet):
    queryset = agendamento.objects.all()
    serializer_class = agendamentoSerializer  

class agendamentoinstrutorViewSet(viewsets.ModelViewSet):
    queryset = agendamentoinstrutor.objects.all()
    serializer_class = agendamentoinstrutorSerializer

class agendamentoclienteViewSet(viewsets.ModelViewSet):
    queryset = agendamentocliente.objects.all()
    serializer_class = agendamentoclienteSerializer
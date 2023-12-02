from django.shortcuts import render
from .models import agendamento, agendamentoaluno, agendamentoinstrutor
from rest_framework import viewsets
from .serializer import agendamentoSerializer, agendamentoalunoSerializer, agendamentoinstrutorSerializer

# Create your views here.

class agendamentoViewSet(viewsets.ModelViewSet):
    queryset = agendamento.objects.all()
    serializer_class = agendamentoSerializer  

class agendamentoalunoViewSet(viewsets.ModelViewSet):
    queryset = agendamentoaluno.objects.all()
    serializer_class = agendamentoalunoSerializer

class agendamentoinstrutorViewSet(viewsets.ModelViewSet):
    queryset = agendamentoinstrutor.objects.all()
    serializer_class = agendamentoinstrutorSerializer


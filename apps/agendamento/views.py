from django.shortcuts import render
from .models import agendamento, agendamentos
from rest_framework import viewsets
from .serializer import agendamentoSerializer, agendamentosSerializer

# Create your views here.

class agendamentoViewSet(viewsets.ModelViewSet):
    queryset = agendamento.objects.all()
    serializer_class = agendamentoSerializer  

class agendamentosViewSet(viewsets.ModelViewSet):
    queryset = agendamentos.objects.all()
    serializer_class = agendamentosSerializer
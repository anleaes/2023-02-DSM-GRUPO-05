from .models import agendamento, agendamentos
from rest_framework import serializers

class agendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamento
        fields = '__all__'
        
class agendamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamentos
        fields = '__all__'

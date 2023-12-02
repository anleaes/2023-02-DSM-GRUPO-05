from .models import agendamento, agendamentoinstrutor, agendamentoaluno
from rest_framework import serializers


class agendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamento
        fields = '__all__'
        
class agendamentoinstrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamentoinstrutor
        fields = '__all__'

class agendamentoalunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamentoaluno
        fields = '__all__'
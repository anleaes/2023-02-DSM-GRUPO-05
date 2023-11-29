from .models import agendamento, agendamentoinstrutor, agendamentocliente
from rest_framework import serializers

class agendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamento
        fields = '__all__'
        
class agendamentoinstrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamentoinstrutor
        fields = '__all__'

class agendamentoclienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamentocliente
        fields = '__all__'

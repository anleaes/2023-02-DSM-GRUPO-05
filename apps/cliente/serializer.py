from .models import cliente, clienteavaliacao
from .models import cliente, clienteplano
from rest_framework import serializers

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'
        
class clienteavaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = clienteavaliacao
        fields = '__all__'

class clienteplanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = clienteplano
        fields = '__all__'
from .models import cliente, clientenivel
from .models import cliente, clienteplano
from rest_framework import serializers

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'
        
class clientenivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientenivel
        fields = '__all__'

class clienteplanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = clienteplano
        fields = '__all__'
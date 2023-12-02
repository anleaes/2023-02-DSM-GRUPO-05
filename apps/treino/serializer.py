from .models import treino, treinoexercicio
from rest_framework import serializers

class treinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = treino
        fields = '__all__'
        
class treinoexercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = treinoexercicio
        fields = '__all__'
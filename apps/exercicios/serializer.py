from .models import exercicio
from rest_framework import serializers

class exercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = exercicio
        fields = '__all__'
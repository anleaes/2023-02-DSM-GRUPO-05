from .models import avaliacao_fisica
from rest_framework import serializers

class avaliacao_fisicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = avaliacao_fisica
        fields = '__all__'
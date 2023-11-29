from .models import avaliacao
from rest_framework import serializers

class avaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = avaliacao
        fields = '__all__'
from .models import plano
from rest_framework import serializers

class planoSerializer(serializers.ModelSerializer):
    class Meta:
        model = plano
        fields = '__all__'
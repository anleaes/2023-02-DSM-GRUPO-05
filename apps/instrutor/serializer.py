from .models import instrutor
from rest_framework import serializers

class instrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = instrutor
        fields = '__all__'
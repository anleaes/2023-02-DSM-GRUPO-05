from .models import nivel
from rest_framework import serializers

class nivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = nivel
        fields = '__all__'
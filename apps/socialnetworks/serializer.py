from .models import Socialnetwork
from rest_framework import serializers

class SocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socialnetwork
        fields = '__all__'
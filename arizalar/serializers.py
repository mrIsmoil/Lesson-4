from rest_framework import serializers
from .models import Ariza


class ArizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ariza
        fields = '__all__'
        
from api.models import Car
from rest_framework import routers, serializers, viewsets # type: ignore
 
class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'model', 'color', 'description']
        
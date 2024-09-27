from api.models import Car, Message, CustomUser
from rest_framework import routers, serializers, viewsets # type: ignore
 
class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'model', 'color', 'description']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'username']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender_id', 'receiver_id', 'text', 'date']
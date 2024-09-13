from api.models import Car, Message, User
from rest_framework import routers, serializers, viewsets # type: ignore
 
class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'model', 'color', 'description']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'username']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender_id', 'receiver_id', 'text', 'date']
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from api.models import Car, Message, CustomUser
from api.serializers import CarSerializer, MessageSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import routers, serializers, viewsets # type: ignore
from rest_framework import mixins
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
class CarList(APIView):

    def get(self, request, format=None):
  
        items = Car.objects.all()
        serializer = CarSerializer(items, many=True)
        
        return Response(serializer.data)

class CarDelete(APIView):
    def delete(self, request, pk):
        Car.objects.get(pk=pk).delete()
        return Response(data="deleted", status=status.HTTP_204_NO_CONTENT)


class CarCreate(APIView):
    def post(self, request, format=None):

        name = request.data.get('name')
        
        if Car.objects.filter(name=name).exists():
            return Response({'error: Car with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(f'created: {serializer.data}', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDeleteUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

class MessageDeleteUpdateRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def UserList(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


from django.shortcuts import render
from api.models import Car
from api.serializers import CarSerializer
from rest_framework.permissions import AllowAny
from rest_framework import routers, serializers, viewsets # type: ignore
from rest_framework import mixins
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response

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



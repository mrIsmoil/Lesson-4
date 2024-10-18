from django.shortcuts import render
from .models import Ariza
from rest_framework import generics, permissions
from .serializers import ArizaSerializer

class AplicationsList(generics.ListAPIView):
    queryset =  Ariza.objects.all()
    serializer_class = ArizaSerializer
    permission_classes = [permissions.IsAuthenticated ]

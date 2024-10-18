from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PhoneVerificationSerializer
from .models import PhoneVerification
from config.utils import send_verification_sms

from elonlar.serializers import JobPostSerializer
from .models import  JobPost

class RequestVerificationCode(APIView):
    def post(self, request):
        serializer = PhoneVerificationSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data('phone_number')
            verification, created= PhoneVerification.objects.get_or_create(phone_number=phone_number)
            verification.generate_verification_code()
            send_verification_sms(phone_number, verification.verification_code)
            return Response({'message':'Verification code sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyCode(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        verification_code = request.data.get('verification_code')

        try:
            verification = PhoneVerification.objects.get(phone_number=phone_number)
            if verification.verification_code == verification_code:
                verification.is_verified = True
                verification.save()
                return Response({'message':'Phone number verified'}, status=status.HTTP_200_OK)
            else:
                return Response({'message':'Wrong verification code'}, status=status.HTTP_400_BAD_REQUEST)
        except PhoneVerification.DoesNotExist:
            return Response({'error':'Phone number not found'}, status=status.HTTP_404_NOT_FOUND )

class Joblist(generics.ListAPIView):
    queryset =  JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [permissions.AllowAny, ]

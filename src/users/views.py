import re
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer 

# Create your views here.


class Register(GenericAPIView):
      serializer_class = RegisterSerializer

      def post(self, request):

        ser = RegisterSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_201_CREATED)

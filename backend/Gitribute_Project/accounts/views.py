from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import DonorCreateSerializer, ReceiverCreateSerializer, UserLoginSerializer
from .models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    if request.method == 'POST':
        num = request.data["role"]
        print(num)

        #num이 1이면 Receiver, 2이면 Donor
        if int(num) == 1:
            print("receiver시리얼라이저")
            serializer = ReceiverCreateSerializer(data=request.data)
        elif int(num) == 2:
            print("donor시리얼라이저")
            serializer = DonorCreateSerializer(data=request.data)
        else:
            print("validated_serializer 오류")

        
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(email=serializer.validated_data['email']).first() is None:
            
            serializer.save()
            print(serializer.data)
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        u=request.data
        print(u)
        serializer = UserLoginSerializer(data=request.data)
        
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'Password Error'}, status=status.HTTP_200_OK)
        if serializer.validated_data['email'] == "NoExist":
            return Response({'message': 'No Email'}, status=status.HTTP_200_OK)
        #if serializer.validate_data['password']

        response = {
            'success': 'True',
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)
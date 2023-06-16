from django.shortcuts import render
from rest_framework.response import Response
from .serializer import UserSignUpSerializer,UserLoginSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
@api_view(["POST"])
def userSignUpView(request):
    serializer = UserSignUpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Sign Up Sucessful",
            "data":serializer.data
        },status=status.HTTP_201_CREATED)
    return Response({
        "error":serializer.errors,
        "data":{}
    },status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def userLoginView(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        token = serializer.create_token(serializer.validated_data)
        return Response(token, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def userLogoutView(request):
    token = request.data.get('token')
    
    if token:
        try:
            # Blacklist the refresh token
            RefreshToken(token).blacklist()
            return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'detail': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)






        

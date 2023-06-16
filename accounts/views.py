from django.shortcuts import render
from rest_framework.response import Response
from .serializer import UserSignUpSerializer
from rest_framework.decorators import api_view
from rest_framework import status

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


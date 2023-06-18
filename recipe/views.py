from django.shortcuts import render
from .serializer import RecipeSerializer
from rest_framework.decorators import permission_classes,api_view,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Recipes

# Create your views here.

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def createRecipe(request):
    data = request.data
    serializer = RecipeSerializer(data=data,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"recipe created"},status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getUserRecipeList(request):
    user = request.user
    recipes = Recipes.objects.filter(chef=user)
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


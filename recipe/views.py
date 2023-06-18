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



@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getRecipe(request):
    title = request.GET.get('title')
    try:
        recipe = Recipes.objects.get(title=title)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    except Recipes.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteRecipe(request):
    try:
        title = request.GET.get('title')
        recipe = Recipes.objects.get(title=title)
        if recipe.chef != request.user:
            return Response({'error': 'You are not authorized to delete this recipe.'}, status=status.HTTP_403_FORBIDDEN)
        
        recipe.delete()
        return Response({'message': 'Recipe deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Recipes.DoesNotExist:
        return Response({'error': 'Recipe not found.'}, status=status.HTTP_404_NOT_FOUND)
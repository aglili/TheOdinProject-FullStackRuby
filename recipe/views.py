from django.shortcuts import render
from .serializer import RecipeSerializer
from rest_framework.decorators import permission_classes,api_view,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe,Like
from accounts.models import CustomUser

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
    recipes = Recipe.objects.filter(chef=user)
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)



@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getRecipe(request):
    title = request.GET.get('title')
    try:
        recipe = Recipe.objects.get(title=title)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteRecipe(request):
    try:
        title = request.GET.get('title')
        recipe = Recipe.objects.get(title=title)
        if recipe.chef != request.user:
            return Response({'error': 'You are not authorized to delete this recipe.'}, status=status.HTTP_403_FORBIDDEN)
        
        recipe.delete()
        return Response({'message': 'Recipe deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Recipe.DoesNotExist:
        return Response({'error': 'Recipe not found.'}, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editRecipe(request):
    try:
        title = request.GET.get('title')
        recipe = Recipe.objects.get(title=title)
        if recipe.chef != request.user:
            return Response({'error': 'You are not authorized to edit this recipe.'}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)
    except Recipe.DoesNotExist:
        return Response({'error': 'Recipe not found.'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
@permission_classes(IsAuthenticated)
def likeRecipe(request):
    recipe_id = request.GET.get('recipe')
    user = request.user
    recipe = Recipe.objects.get(id=recipe_id)
    like = Like(user=user, recipe=recipe)
    like.save()
    return Response({
        "message":"Recipe Liked"
    },status=status.HTTP_201_CREATED)
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLikedRecipes(request):
    user = CustomUser.objects.get(id=request.user)
    liked_recipes = user.liked_recipes.all()
    serializer = RecipeSerializer(liked_recipes,many=True)
    return Response({
        "liked recipes" : serializer.data,
    },status=status.HTTP_200_OK)

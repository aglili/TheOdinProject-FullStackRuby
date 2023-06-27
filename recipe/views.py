from django.shortcuts import render
from .serializer import RecipeSerializer
from rest_framework.decorators import permission_classes,api_view,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe,Like
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def createRecipe(request):
    data = request.data
    serializer = RecipeSerializer(data=data,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"recipe created",
            "data":serializer.data},status=status.HTTP_200_OK)
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def likeRecipe(request):
    try:
        recipe_id = request.GET.get('recipe_id')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user = request.user
        like, created = Like.objects.get_or_create(chef=user, recipe=recipe)
        if created:
            return Response({
                "message": "Recipe liked"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "Recipe already liked"
            }, status=status.HTTP_200_OK)
    except Recipe.DoesNotExist:
        return Response({
            "error": "Recipe not found"
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def unlikeRecipe(request):
    try:
        recipe_id = request.GET.get('recipe_id')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user = request.user
        like = Like.objects.filter(chef=user, recipe=recipe)
        if like.exists():
            like.delete()
            return Response({
                "message": "Recipe unliked"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "Recipe was not liked by the user"
            }, status=status.HTTP_200_OK)
    except Recipe.DoesNotExist:
        return Response({
            "error": "Recipe not found"
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getLikedRecipesByUser(request):
    try:
        user = request.user
        liked_recipes = Recipe.objects.filter(likes__username=user.username)
        serializer = RecipeSerializer(liked_recipes, many=True)
        return Response({
            "liked_recipes": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





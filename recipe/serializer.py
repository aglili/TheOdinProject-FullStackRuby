from rest_framework import serializers
from .models import Recipe,Like







class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id','title','instructions','diet_type','meal_type','difficulty','time','food_image']


    def create(self, validated_data):
        chef = self.context['request'].user
        recipe = Recipe.objects.create(
            title=validated_data['title'],
            instructions=validated_data['instructions'],
            diet_type=validated_data['diet_type'],
            meal_type=validated_data['meal_type'],
            difficulty=validated_data['difficulty'],
            time=validated_data['time'],
            food_image=validated_data['food_image'],
            chef = chef
        )
        recipe.save()
        return 
    


class LikedRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'recipe']

from django.db import models
from accounts.models import CustomUser


   






class Recipes(models.Model):
    RECIPE_CATEGORY = [
        ("french", "French"),
        ("italian", "Italian"),
        ("indian", "Indian"),
        ("ghanaian","Ghanian"),
    ]

    DIET_CATEGORY = [
        ("vegetarian", "Vegetarian"),
        ("vegan", "Vegan"),
        ("pescatarian", "Pescatarian"),
        ("gluten-free", "Gluten-Free"),
        ("dairy-free", "Dairy-Free"),
    ]

    DIFFICULTY_LEVEL = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    category = models.CharField(max_length=100,choices=RECIPE_CATEGORY)
    chef = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    diet = models.CharField(max_length=100,choices=DIET_CATEGORY)
    difficulty = models.CharField(max_length=100,choices=DIFFICULTY_LEVEL)
    time = models.DurationField()
    food_image = models.ImageField(upload_to='food/images')

    def __str__(self) -> str:
        return f"Recipe:{self.title} by Chef{self.chef.username}"
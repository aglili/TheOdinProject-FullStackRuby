from django.db import models
from accounts.models import CustomUser


   






class Recipe(models.Model):
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

    MEAL_TYPE =[
        ("breakfast","Breakfast"),
        ("brunch","Brunch"),
        ("lunch","Lunch"),
        ("snack","Snack"),
        ("supper","Supper"),
        ("dessert","Dessert")
    ]

    
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    chef = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    diet_type = models.CharField(max_length=100,choices=DIET_CATEGORY)
    meal_type = models.CharField(max_length=100,choices=MEAL_TYPE,default="")
    difficulty = models.CharField(max_length=100,choices=DIFFICULTY_LEVEL)
    time = models.DurationField()
    food_image = models.ImageField(upload_to='food/images')
    

    def __str__(self) -> str:
        return f"Recipe:{self.title} by Chef {self.chef.username}"
    


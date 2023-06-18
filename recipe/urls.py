from django.urls import path
from . import views


urlpatterns = [
    path("create/",views.createRecipe,name='create_recipe'),
    path("user/all",views.getUserRecipeList,name='get_user_recipe_list')
]
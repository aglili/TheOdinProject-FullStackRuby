from django.urls import path
from . import views


urlpatterns = [
    path("create/",views.createRecipe,name='create_recipe'),
    path("all/",views.getUserRecipeList,name='get_user_recipe_list'),
    path("get-recipe/",views.getRecipe,name='get_recipe_by_title'),
    path("delete/",views.deleteRecipe,name="delete_recipe_by_title"),
    path("edit/",views.editRecipe,name="update_recipe_by_title"),

]
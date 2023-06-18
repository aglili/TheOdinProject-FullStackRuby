from django.urls import path
from . import views


urlpatterns = [
    path("create/",views.createRecipe,name='create_recipe')
]
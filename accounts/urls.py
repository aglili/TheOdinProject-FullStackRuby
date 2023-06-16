from django.urls import path
from . import views


urlpatterns = [
    path("signup/",views.userSignUpView,name='sign-up'),
    path('login/',views.userLoginView,name='login'),
    
]
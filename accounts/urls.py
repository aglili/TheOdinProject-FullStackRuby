from django.urls import path
from . import views


urlpatterns = [
    path("signup/",views.userSignUpView,name='sign_up'),
    path('login/',views.userLoginView,name='login'),
    path('logout/',views.userLogoutView,name='logout')
    
]
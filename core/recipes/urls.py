from django.urls import path
from .views import *

urlpatterns = [
    path('' , home ,name='home' ),
    path('recipes/' ,recipe_add ,name='recipe_add' ),
    path('recipe_delete/<id>/' ,recipe_delete , name='recipe_delete' ),
    path('recipe_update/<id>/' ,recipe_update, name='recipe_delete' ),
    path('register/' , register ,name="register"),
    path('login/' , login_page ,name="login"),
    path('logout/' , logout_page ,name="logout_page"),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('' ,recipe_add ,name='recipe_add' ),
    path('recipe_delete/<id>/' ,recipe_delete , name='recipe_delete' ),
    path('recipe_update/<id>/' ,recipe_update, name='recipe_delete' ),
    
]
from django.shortcuts import render ,redirect
from .models import Recipe

def recipe_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES['image']
        Recipe.objects.create(name = name , description = description , image = image)
    
    recipes = Recipe.objects.all()
    context = {'recipes' : recipes}      
    return render(request, 'recipes_ui.html' , context)


def recipe_update(request ,id):
    query_set = Recipe.objects.get(id = id)
    
    if request.method == 'POST':      
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES['image']

        query_set.name = name
        query_set.description = description

        if query_set.image:
         query_set.image = image

        query_set.save()  

        return redirect('/') 

    context = {'recipes' : query_set} 
    return render(request , 'update_recipe.html' , context)


def recipe_delete(request , id):
    query_set = Recipe.objects.get(id = id)
    query_set.delete()
    return redirect('/')
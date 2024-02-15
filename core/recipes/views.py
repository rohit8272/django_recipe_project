from django.shortcuts import render ,redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request , 'index.html')

@login_required(login_url='/login')
def recipe_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES['image']
        Recipe.objects.create(name = name , description = description , image = image)

    recipes = Recipe.objects.all()

    if request.GET.get('search'):
        recipes = recipes.filter(name__icontains = request.GET.get('search'))

    context = {'recipes' : recipes}      
    return render(request, 'recipes_ui.html' , context)

@login_required(login_url='/login')
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

        return redirect('/recipes') 

    context = {'recipes' : query_set} 
    return render(request , 'update_recipe.html' , context)

@login_required(login_url='/login')
def recipe_delete(request , id):
    query_set = Recipe.objects.get(id = id)
    query_set.delete()
    return redirect('/recipes')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = User.objects.filter(username = username).exists()

        if not user:
           messages.info(request, "user not exist")
           return redirect('/register')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.error(request, "invalid credentials")
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/recipes')

    return render(request , 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "user already exist")
            return redirect('/register')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "user registered successfully !")
        return redirect('/register')

    return render(request , 'register.html')
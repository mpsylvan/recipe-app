from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.

def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"

class RecipeDetail(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"
    
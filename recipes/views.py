from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

# Create your views here.

def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"

class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

def records(request):
    return render(request, 'recipes/records.html')
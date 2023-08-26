from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ingredient
# Create your views here.

class IngredientsList(ListView):
    model = Ingredient
    template_name = 'ingredients/ing.html'

class IngredientsDetail(DetailView):
    model = Ingredient
    template_name = 'ingredients/ingd.html'
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ingredient
# Create your views here.

class IngredientsList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'ingredients/ing.html'

class IngredientsDetail(LoginRequiredMixin, DetailView):
    model = Ingredient
    template_name = 'ingredients/ingd.html'
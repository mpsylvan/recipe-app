from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ingredient

# Create your views here.


class IngredientsList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "ingredients/ing.html"


class IngredientsDetail(LoginRequiredMixin, DetailView):
    model = Ingredient
    template_name = "ingredients/ingd.html"


class IngredientInput(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "ingredients/ingredient_input.html"
    fields = ["name", "uom"]

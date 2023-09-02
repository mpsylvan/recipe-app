from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from ingredients.models import Ingredient
from .forms import RecipeInputForm, IngredientInputForm, RecipeSearchForm
import pandas as pd

# Create your views here.


def home(request):
    return render(request, "recipes/recipes_home.html")


class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"


class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail.html"


@login_required
def records(request):
    form = RecipeSearchForm(request.POST or None)
    name = None
    chart_type = None

    if request.method == "POST":
        name = request.POST.get("name")
        chart_type = request.POST.get("chart_type")

    if name == "a":
        qs = Recipe.objects.all()
        for recipe in qs:
            print(recipe.name)
    elif name == "b":
        qs = Recipe.objects.all()
        for recipe in qs:
            print(recipe.cooking_time)
    elif name == "c":
        qs = Recipe.objects.filter(name__contains="bake")
        for recipe in qs:
            print(recipe)
    context = {
        "form": form,
    }

    return render(request, "recipes/records.html", context)


@login_required
def recipe_input(request):
    form = RecipeInputForm(request.POST or None)
    ingredient_form = IngredientInputForm(request.POST or None)

    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     cooking_time = request.POST.get("cooking_time")
    #     ingredients = request.POST.get("ingredients")
    #     new_ingredient = request.POST.get("add_ingredient_name")

    context = {"form": form, "ingredient_form": ingredient_form}
    return render(request, "recipes/recipe_input.html", context)

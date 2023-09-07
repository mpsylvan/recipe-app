from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from ingredients.models import Ingredient
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_chart

# Create your views here.


def home(request):
    return render(request, "recipes/recipes_home.html")


def about(request):
    return render(request, "recipes/about.html")


class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"


class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail.html"


@login_required
def records(request):
    form = RecipeSearchForm(request.POST or None)
    chart = None
    df = None

    if request.method == "POST":
        name = request.POST.get("name")
        limit = request.POST.get("ingredients_limit")
        # chart_type = request.POST.get("chart_type")
        qs_recipes = Recipe.objects.all()
        qs_ingredients = Ingredient.objects.all()
        if qs_recipes and qs_ingredients:
            if name == "#1":
                df = pd.DataFrame(qs_recipes.values())
                chart = get_chart("a", df, labels=df["name"].values)
                df = df.to_html()

            elif name == "#2":
                ingredients_to_quantity = ()
                for ingredient in qs_ingredients:
                    ingredients_to_quantity = (
                        (ingredient.name, len(ingredient.recipe_set.all())),
                    ) + ingredients_to_quantity
                df = pd.DataFrame(
                    ingredients_to_quantity, columns=["name", "recipes_in"]
                ).sort_values("recipes_in", ascending=False)
                if limit:
                    df = df[: int(limit)]
                chart = get_chart("b", df, labels=df["name"].values)
                df = None
            elif name == "#3":
                df = pd.DataFrame(qs_recipes.values())
                df["difficulty"] = [object.calc_difficulty() for object in qs_recipes]
                difficulties = df["difficulty"].value_counts()
                chart = get_chart("c", difficulties)
                df = df.to_html()
            else:
                print("working on it. ")
    else:
        print("issue with post request. ")

    context = {"form": form, "df": df, "chart": chart}

    return render(request, "recipes/records.html", context)


class RecipeInput(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/recipe_input.html"
    fields = ["name", "cooking_time", "ingredients"]

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


"""authorized functional view that includes a builtin django form for request data from the model and rendering visualizations.

    args: the http request object

    returns: a rendered http response of form template that has context for data and pyplot graph.

"""


@login_required
def records(request):
    form = RecipeSearchForm(request.POST or None)
    chart = None
    df = None

    if request.method == "POST":
        name = request.POST.get("name")
        # stores the limit on results returned in the ingredients wheel.
        limit = request.POST.get("ingredients_limit")
        # chart_type = request.POST.get("chart_type")
        qs_recipes = Recipe.objects.all()
        qs_ingredients = Ingredient.objects.all()
        if qs_recipes and qs_ingredients:
            if name == "#1":
                df = pd.DataFrame(qs_recipes.values())
                # builds a chart with 'a' to trigger a line graph.
                chart = get_chart("a", df, labels=df["name"].values)
                df = df.to_html()
            elif name == "#2":
                # empty tuple that gets filled with tuples of ingredients and their recipes.
                ingredients_to_quantity = ()
                # loops over the full queryset of ingredients in the db and adds respective ingredients (name, recipe count).
                for ingredient in qs_ingredients:
                    ingredients_to_quantity = (
                        (ingredient.name, len(ingredient.recipe_set.all())),
                    ) + ingredients_to_quantity
                # makes a dataframe out of the tuple of tuples created above.
                df = pd.DataFrame(
                    ingredients_to_quantity, columns=["name", "recipes_in"]
                ).sort_values("recipes_in", ascending=False)
                # checks if a limit was entered into the form
                if limit:
                    df = df[: int(limit)]
                # builds a chart with 'b' to trigger a pie graph
                chart = get_chart("b", df, labels=df["name"].values)
                # sets df to None to prevent a render.
                df = None
            elif name == "#3":
                df = pd.DataFrame(qs_recipes.values())
                # makes a new column that is the difficulty rating of each respective recipe
                df["difficulty"] = [object.calc_difficulty() for object in qs_recipes]
                # makes a Series object tallying up counts/difficulty
                difficulties = df["difficulty"].value_counts()
                # builds a chart with 'c' to trigger a bar graph.
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

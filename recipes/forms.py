from django import forms
from .models import Recipe
from ingredients.models import Ingredient


CONTENT_CHOICES = (
    ("a", "Recipes"),
    ("b", "CookingTime"),
    ("c", "Difficulty"),
    ("d", "Ingredients"),
)

CHART_CHOICES = (
    ("a", "Bar"),
    ("b", "Graph"),
    ("c", "Line"),
)


class RecipeSearchForm(forms.Form):
    name = forms.ChoiceField(choices=CONTENT_CHOICES)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)


class RecipeInputForm(forms.Form):
    name = forms.CharField(max_length=20)
    cooking_time = forms.IntegerField(min_value=1)
    ingredients = forms.ModelMultipleChoiceField(Ingredient.objects.all())


class IngredientInputForm(forms.Form):
    new_ingredient_name = forms.CharField(max_length=50)
    new_ingredient_UOM = forms.ChoiceField(choices=Ingredient.units_of_measure)

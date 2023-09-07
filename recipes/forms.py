from django import forms
from .models import Recipe
from ingredients.models import Ingredient


CONTENT_CHOICES = (
    ("#1", "Recipes (cooktime line graph)"),
    ("#2", "Ingredients (frequency wheel)"),
    ("#3", "Difficulty (bar graph)"),
)

# CHART_CHOICES = (
#     ("a", "Bar"),
#     ("b", "Graph"),
#     ("c", "Line"),
# )


class RecipeSearchForm(forms.Form):
    name = forms.ChoiceField(choices=CONTENT_CHOICES)
    # chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    ingredients_limit = forms.IntegerField(
        help_text="(^leave blank to display all recipes, 5 - 20 ingredients)",
        required=False,
        min_value=5,
        max_value=20,
    )

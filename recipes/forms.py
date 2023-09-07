from django import forms
from .models import Recipe
from ingredients.models import Ingredient

#  tuple of tuples of choices for which type of data is being pulled and used when forming a dataframe and visualization.
CONTENT_CHOICES = (
    ("#1", "Recipes (cooktime line graph)"),
    ("#2", "Ingredients (frequency wheel)"),
    ("#3", "Difficulty (bar graph)"),
)


# the name choice will get parsed in the form view to specify data output.
class RecipeSearchForm(forms.Form):
    name = forms.ChoiceField(choices=CONTENT_CHOICES)
    ingredients_limit = forms.IntegerField(
        help_text="(^leave blank to display all recipes, 5 - 20 ingredients)",
        required=False,
        min_value=5,
        max_value=20,
        initial=10,
    )

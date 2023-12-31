from django.db import models
from ingredients.models import Ingredient
from django.shortcuts import reverse

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveIntegerField(help_text="(minutes)")
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    # builds an aboslute url to provide linkage to the specific recipe
    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    # access a query set of all ingredients to be able to display the ingredients on a details page.
    def get_ingredients(self):
        ingredient_objects = self.ingredients.all()
        return ingredient_objects

    # evaluates the difficulty of a recipe by checking ingredients length and cooking time against conditions.
    def calc_difficulty(self):
        new_difficulty = ""
        ingredients = self.get_ingredients()
        if self.cooking_time < 15 and len(ingredients) < 5:
            new_difficulty = "Easy"
        elif self.cooking_time < 15 and len(ingredients) >= 5:
            new_difficulty = "Medium"
        elif self.cooking_time >= 15 and len(ingredients) <= 5:
            new_difficulty = "Intermediate"
        elif self.cooking_time >= 15 and len(ingredients) >= 5:
            new_difficulty = "Hard"
        return new_difficulty

    def __str__(self):
        return f"{self.name}"

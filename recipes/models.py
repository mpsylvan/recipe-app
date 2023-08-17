from django.db import models
from ingredients.models import Ingredient

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveIntegerField(help_text='(minutes)')
    difficulty = models.CharField(max_length = 20, default="n/a")
    ingredients = models.ManyToManyField(Ingredient, blank=True)


    def __str__(self):
        return f'{self.name}'
    
    



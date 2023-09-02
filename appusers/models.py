from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# Create your models here.

# Create your models here.
class AppUser(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe, blank=True)


    def __str__(self):
        return f'{self.username}'
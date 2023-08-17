from django.test import TestCase
from .models import Recipe
from ingredients.models import Ingredient

# Create your tests here.


class RecipeModelTest(TestCase):

    def setUpTestData():

        ing1 = Ingredient(
            name = 'Butter',
            uom = 'Tablespoon',
        )

        ing1.save()


        recipe1 = Recipe.objects.create(
            name = "Popcorn",
            cooking_time = 5, 
            difficulty = "Easy",
            
        )

        recipe1.save()

        recipe1.ingredients.add(ing1)

    

    
    def test_recipe_name(self):
        # pull the first recipe from the test db.
        recipe1 = Recipe.objects.get(id=1)

        field_name = recipe1._meta.get_field('name').verbose_name
        self.assertEqual(field_name, 'name')
    
    def test_recipe_difficulty_max_length(self):
        # pull the first recipe from the test db.
        recipe1 = Recipe.objects.get(id=1)

        max_length = recipe1._meta.get_field('difficulty').max_length
        self.assertEqual(max_length, 20)

    def test_recipe_cooking_time_integer(self):
        # pull the first recipe from the test db.
        recipe1 = Recipe.objects.get(id=1)

        field = recipe1._meta.get_field('cooking_time').db_column
        print(field)

    def test_recipe_ingredients_relationship(self):
        recipe1= Recipe.objects.get(id=1)
        many_to_many = recipe1._meta.get_field('ingredients').many_to_many
        self.assertTrue(many_to_many)

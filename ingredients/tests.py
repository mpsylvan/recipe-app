from django.test import TestCase
from .models import Ingredient


# Create your tests here.

class IngredientModelTest(TestCase):

    def setUpTestData():

        Ingredient.objects.create(
            name = 'Butter',
            uom = 'Tablespoon'
        )

    def test_ingredients_name_length(self):

        ing1 = Ingredient.objects.get(name ='Butter')

        max_length = ing1._meta.get_field('name').max_length

        self.assertEqual(max_length, 50)


    def test_ingredients_uom_can_be_blank(self):

        ing1 = Ingredient.objects.get(name ='Butter')

        blank = ing1._meta.get_field('uom').blank

        self.assertTrue(blank)

    def test_ingredients_uom_choices(self):
        
        ing1 = Ingredient.objects.get(name ='Butter')

        uom_choices = ing1._meta.get_field('uom').choices
        uom_human_readable = [pair[1] for pair in uom_choices ]
        self.assertIn(ing1.uom, uom_human_readable)

    def test_ingredients_uom_length(self):

        ing1 = Ingredient.objects.get(name ='Butter')

        max_length = ing1._meta.get_field('uom').max_length

        self.assertEqual(max_length, 20)
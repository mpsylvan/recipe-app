from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe
from ingredients.models import Ingredient
from .forms import RecipeSearchForm
from django.contrib.auth.models import User


# Create your tests here.


class RecipeInputTest(TestCase):
    def setUpTestData():
        credentials = {"username": "tester", "password": "secret"}

        User.objects.create_user(**credentials)

        ing1 = Ingredient(
            name="Butter",
            uom="Tablespoon",
        )

        ing1.save()

    def test_users(self):
        c = Client()
        c.login(username="tester", password="secret")

        self.assertEqual(
            User.objects.last().username,
            "tester",
        )

    def test_recipe_createview(self):
        c = Client()
        c.login(username="tester", password="secret")
        response = c.post(
            reverse("recipes:recipe-input"), {"name": "magic pepper", "cooking_time": 5}
        )
        self.assertEqual(Recipe.objects.last().name, "magic pepper")
        self.assertEqual(Recipe.objects.last().cooking_time, 5)

    def test_ingredient_createview(self):
        c = Client()
        c.login(username="tester", password="secret")
        response = c.post(
            reverse("ingredients:ingredient-input"),
            {"name": "magic pepper", "uom": "Leaf"},
        )


class RecipeFormTest(TestCase):
    def test_form_renders_inputs(self):
        form = RecipeSearchForm()
        self.assertIn("name", form.as_p())
        self.assertIn("ingredients_limit", form.as_p())

    def test_ingredients_limit_help_text(self):
        form = RecipeSearchForm()
        self.assertEqual(
            form.fields["ingredients_limit"].help_text,
            "(^leave blank to display all recipes, minimum results is 5)",
        )

    def test_ingredients_required_false(self):
        form = RecipeSearchForm()
        self.assertEqual(form.fields["ingredients_limit"].required, False)

    def test_form_url(self):
        form = RecipeSearchForm()
        response = self.client.get("/records")
        self.assertEqual(response.status_code, 302)


class RecipeModelTest(TestCase):
    def setUpTestData():
        ing1 = Ingredient(
            name="Butter",
            uom="Tablespoon",
        )

        ing1.save()

        recipe1 = Recipe.objects.create(
            name="Popcorn",
            cooking_time=5,
        )

        recipe1.save()

        recipe1.ingredients.add(ing1)

    def test_recipe_name(self):
        # pull the first recipe from the test db.
        recipe1 = Recipe.objects.get(id=1)

        field_name = recipe1._meta.get_field("name").verbose_name
        self.assertEqual(field_name, "name")

    def test_recipe_difficulty_calc(self):
        # pull the first recipe from the test db.
        recipe1 = Recipe.objects.get(id=1)

        recipe1_difficulty = recipe1.calc_difficulty()
        self.assertEqual(recipe1.calc_difficulty(), "Easy")

    def test_recipe_cooking_time_integer(self):
        # pull the first recipe from the test db.
        recipe1 = Recipe.objects.get(id=1)

        field = recipe1._meta.get_field("cooking_time").db_column

    def test_recipe_ingredients_relationship(self):
        recipe1 = Recipe.objects.get(id=1)
        many_to_many = recipe1._meta.get_field("ingredients").many_to_many
        self.assertTrue(many_to_many)

    def test_recipe_absolute_url(self):
        recipe1 = Recipe.objects.get(id=1)
        self.assertEqual(recipe1.get_absolute_url(), "/list/1")

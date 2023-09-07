from django.db import models
from django.shortcuts import reverse


# Create your models here.


class Ingredient(models.Model):
    units_of_measure = (
        ("tbsp", "Tablespoon"),
        ("tsp", "Teaspoon"),
        ("clove", "Clove"),
        ("slice", "Slice"),
        ("oz", "Ounce"),
        ("g", "Gram"),
        ("pc", "Piece"),
        ("half", "Half"),
        ("bag", "Bag"),
        ("cup", "Cup"),
        ("wedge", "Wedge"),
        ("pinch", "Pinch"),
        ("lb", "Pound"),
        ("lf", "Leaf"),
    )

    name = models.CharField(max_length=50)
    uom = models.CharField(
        max_length=20, default=None, blank=True, choices=units_of_measure
    )  # unit of measure
    pic = models.ImageField(upload_to="ingredients", default="drawing.svg")

    # builds an absolute path to a specific ingredient utlizing the name url param and the db primary of each ingredient.
    def get_absolute_url(self):
        return reverse("ingredients:ingd", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"

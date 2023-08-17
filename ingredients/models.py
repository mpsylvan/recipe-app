from django.db import models

# Create your models here.

class Ingredient(models.Model):

    units_of_measure = (
        ('tbsp', 'Tablespoon'),
        ('tsp', 'Teaspoon'),
        ('clove', 'Clove'),
        ('slice', 'Slice'),
        ('oz', 'Ounce'),
        ('g', 'Gram'),
        ('pc', 'Piece'),
        ('half', 'Half'),
        ('bag', 'Bag'),
        ('cup', 'Cup'),
        ('wedge', 'Wedge'),
        ('pinch', 'Pinch'),
        ('lb', 'Pound')
    )

    name = models.CharField(max_length=50)
    uom = models.CharField(max_length=20, default=None, blank=True, choices=units_of_measure) # unit of measure

    def __str__(self):
        return f'{self.name}'
# Generated by Django 4.2.4 on 2023-08-17 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
        ('recipes', '0002_remove_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='ingredients.ingredient'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(help_text='(minutes)'),
        ),
    ]

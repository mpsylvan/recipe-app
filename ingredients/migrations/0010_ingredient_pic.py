# Generated by Django 4.2.4 on 2023-08-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0009_alter_ingredient_uom'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='pic',
            field=models.ImageField(default='drawing.svg', upload_to='ingredients'),
        ),
    ]
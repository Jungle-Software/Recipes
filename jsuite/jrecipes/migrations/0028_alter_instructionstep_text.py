# Generated by Django 4.0.4 on 2023-01-04 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jrecipes', '0027_remove_ingredientlistitem_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructionstep',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 4.0.4 on 2023-01-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jrecipes', '0020_rename_allergen_ingredient_allergens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='instructions',
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.ManyToManyField(to='jrecipes.instructionstep'),
        ),
    ]

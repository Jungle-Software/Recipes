# Generated by Django 4.0.4 on 2022-09-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jrecipes', '0002_allergen_category_remove_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='allergens',
            field=models.ManyToManyField(blank=True, to='jrecipes.allergen'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='parentSubRecipe',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='additional_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(blank=True, help_text='Select a category for this recipe', to='jrecipes.category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, help_text='Select an ingredient for this recipe', to='jrecipes.recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='nutritional_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='portion_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]

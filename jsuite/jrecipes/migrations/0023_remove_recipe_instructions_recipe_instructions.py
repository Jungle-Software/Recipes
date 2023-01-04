# Generated by Django 4.0.4 on 2023-01-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jrecipes', '0022_remove_recipe_instructions_recipe_instructions'),
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
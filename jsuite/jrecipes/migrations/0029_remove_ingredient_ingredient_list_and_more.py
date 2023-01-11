# Generated by Django 4.0.4 on 2023-01-05 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jrecipes', '0028_alter_instructionstep_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='ingredient_list',
        ),
        migrations.AddField(
            model_name='ingredientlistitem',
            name='ingredient',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_list_item', to='jrecipes.ingredient'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.4 on 2023-01-03 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jrecipes', '0016_alter_ingredientlistitem_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientlistitem',
            name='ingredient',
            field=models.OneToOneField(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='jrecipes.ingredient'),
            preserve_default=False,
        ),
    ]

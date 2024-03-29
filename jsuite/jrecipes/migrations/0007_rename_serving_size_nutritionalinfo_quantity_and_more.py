# Generated by Django 4.0.4 on 2022-09-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jrecipes', '0006_remove_nutritionalunit_serving_size_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutritionalinfo',
            old_name='serving_size',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='nutritionalinfo',
            name='nutritional_unit',
        ),
        migrations.AddField(
            model_name='nutritionalinfo',
            name='unit',
            field=models.CharField(choices=[('mg', 'Milligram'), ('g', 'Gram'), ('kg', 'Kilogram')], default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NutritionalUnit',
        ),
    ]

# Generated by Django 4.0.4 on 2022-09-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jrecipes', '0004_nutritionalunit_nutritionalinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionalunit',
            name='unit',
            field=models.CharField(choices=[('mg', 'Milligram'), ('g', 'Gram'), ('kg', 'Kilogram')], max_length=4),
        ),
    ]

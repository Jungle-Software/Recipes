# Generated by Django 4.0.4 on 2022-09-12 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jrecipes', '0013_rename_portion_size_recipe_servings_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructionStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('sub_steps', models.ManyToManyField(blank=True, to='jrecipes.instructionstep')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction_steps', models.ManyToManyField(to='jrecipes.instructionstep')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jrecipes.instruction'),
        ),
    ]

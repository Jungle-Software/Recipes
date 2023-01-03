from django.db import models
from django.utils.translation import gettext as _

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Allergen(models.Model):
    type = models.CharField(max_length=150)  # Nuts, Lactose, etc...

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.type


'''
class NutritionalInfo(models.Model):

    quantity = models.IntegerField()
    unit = models.CharField(
        max_length=20,
        choices=UnitType.choices,
    )
    calories = models.IntegerField()

    def __str__(self):
        return str(self.quantity) + self.unit + ' per Serving Calories: ' + str(self.calories)
'''

class InstructionStep(models.Model):
    text = models.TextField()
    #image = models.ImageField(upload_to=None, blank=True) # TODO FIX IMAGES LATER
    sub_steps = models.ManyToManyField('self', blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text

'''
class Instruction(models.Model):
    instruction_steps = models.ManyToManyField(InstructionStep)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "Nothing yet fix this" # TODO
'''

class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    allergen = models.ManyToManyField(Allergen, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class IngredientListItem(models.Model):

    class UnitType(models.TextChoices):
        # TODO add way to do something like 2 Whole banana if the ingredient is a banana for example
        unit = 'unit', _('un')
        milligram = 'milligram', _('mg')
        gram = 'gram', _('g')
        kilogram = 'kilogram', _('Kg')
        milliliter = 'milliliter', _('mL')
        liter = 'liter', _('L')
        pound = 'pound', _('lb')
        ounce = 'ounce', _('oz')
        fluid_once = 'fluid_once', _('fl oz')
        teaspoon = 'teaspoon', _('tsp')
        tablespoon = 'tablespoon', _('Tbsp')
        cup = 'cup', _('cup')
        pint = 'pint', _('pint')
        quart = 'quart', _('quart')
        gallon = 'gallon', _('gallon')

    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    unit = models.CharField(
        max_length=20,
        choices=UnitType.choices,
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=4)  # Used decimal instead of float, see https://docs.python.org/3/library/decimal.html#module-decimal

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.ingredient.name


class Recipe(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, help_text='Select a category for this recipe', blank=True)
    servings = models.IntegerField(blank=True, null=True)
    prep_time = models.IntegerField(blank=True, null=True)  # In minutes
    cook_time = models.IntegerField(blank=True, null=True)  # In minutes
    ingredient_list = models.ManyToManyField(IngredientListItem, help_text='Select an IngredientListItem for this recipe', blank=True)
    allergens = models.ManyToManyField(Allergen, blank=True)
    instructions = models.OneToOneField(InstructionStep, on_delete=models.CASCADE)
    additional_notes = models.TextField(blank=True)
    date_updated = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

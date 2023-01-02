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
    #image = models.ImageFIeld(upload_to=None, blank=True) # TODO FIX IMAGES LATER
    sub_steps = models.ManyToManyField('self', blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text

class Instruction(models.Model):
    instruction_steps = models.ManyToManyField(InstructionStep)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "Nothing yet fix this" # TODO

class Recipe(models.Model):

    class TypeEnum(models.TextChoices):
        recipe = 'recipe', _('Recipe')
        subRecipe = 'subRecipe', _('Recipe and ingredient')
        ingredient = 'ingredient', _('Ingredient')

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, help_text='Select a category for this recipe', blank=True)
    servings = models.IntegerField(blank=True, null=True)
    prep_time = models.IntegerField(blank=True, null=True)  # In minutes
    cook_time = models.IntegerField(blank=True, null=True)  # In minutes
    ingredients = models.ManyToManyField('self', help_text='Select an ingredient for this recipe', blank=True)
    allergens = models.ManyToManyField(Allergen, blank=True)
    instructions = models.OneToOneField(Instruction, on_delete=models.CASCADE)
    additional_notes = models.TextField(blank=True)
    nutritional_info = models.OneToOneField(NutritionalInfo, on_delete=models.CASCADE)
    type_enum = models.CharField(
        max_length=20,
        choices=TypeEnum.choices,
        default=TypeEnum.recipe,
    ) # 0=Parent recipe only 1=Parent and Ingredient 2=Ingredient
    date_created = models.DateField(auto_now_add=True)

    #def calculateCalories(self):
    #    for x in self.ingredients.get_queryset():
    #        caloriesCount += x.calories
    #    return caloriesCount

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

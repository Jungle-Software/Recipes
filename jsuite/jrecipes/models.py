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

class InstructionStep(models.Model):
    recipe = models.ForeignKey("Recipe", related_name="steps", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    #image = models.ImageField(upload_to=None, blank=True) # TODO FIX IMAGES LATER
    # TODO ADD ORDERFIELD INT !!! V2 !!!

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.text

class InstructionSubStep(models.Model):
    # TODO TEST STRING FIELD NAME
    step = models.ForeignKey("InstructionStep", related_name="sub_steps", on_delete=models.CASCADE)
    text = models.TextField()
    # TODO ADD ORDERFIELD INT !!! V2 !!!

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.text

class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    allergens = models.ManyToManyField("Allergen", blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class UnitType(models.TextChoices):
    # TODO maybe move UnitType outside so it can be used elsewhere?
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

class IngredientListItem(models.Model):
    recipe = models.ForeignKey("Recipe", related_name="ingredient_list_item", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", related_name="ingredient_list_item", on_delete=models.CASCADE)
    unit = models.CharField(
        max_length=20,
        choices=UnitType.choices,
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=4)  # Used decimal instead of float, see https://docs.python.org/3/library/decimal.html#module-decimal

    class Meta:
        ordering = ['-id']

    def __str__(self):
        ingredient_str = str(self.quantity) + " " + self.unit + " " + self.ingredient.name
        return ingredient_str

class Recipe(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField("Category", help_text='Select a category for this recipe', blank=True)
    servings = models.IntegerField(blank=True, null=True)
    prep_time = models.IntegerField(blank=True, null=True)  # In minutes
    cook_time = models.IntegerField(blank=True, null=True)  # In minutes
    allergens = models.ManyToManyField("Allergen", blank=True)
    additional_notes = models.TextField(blank=True)
    date_updated = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

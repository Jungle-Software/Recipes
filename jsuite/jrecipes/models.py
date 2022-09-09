from django.db import models


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


class NutritionalUnit(models.Model):



    def __str__(self):
        return self.unit


class NutritionalInfo(models.Model):

    class UnitType(models.TextChoices):
        milligram = 'mg'
        gram = 'g'
        kilogram = 'kg'

    quantity = models.IntegerField()
    unit = models.CharField(
        max_length=4,
        choices=UnitType.choices,
    )
    calories = models.IntegerField()

    def __str__(self):
        return str(self.serving_size) + self.unit


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, help_text='Select a category for this recipe', blank=True)
    portion_size = models.IntegerField(blank=True, null=True)
    prep_time = models.IntegerField(blank=True, null=True)  # In minutes
    cook_time = models.IntegerField(blank=True, null=True)  # In minutes
    ingredients = models.ManyToManyField('self', help_text='Select an ingredient for this recipe', blank=True)
    allergens = models.ManyToManyField(Allergen, blank=True)
    instructions = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)
    nutritional_info = models.OneToOneField(NutritionalInfo, on_delete=models.CASCADE)
    parentSubRecipe = models.IntegerField() # 0=Parent recipe only 1=Parent and Ingredient 2=Ingredient
    date_created = models.DateField(auto_now_add=True)

    #def calculateCalories(self):
    #    for x in self.ingredients.get_queryset():
    #        caloriesCount += x.calories
    #    return caloriesCount

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

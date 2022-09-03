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
    

'''
class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    calories = models.IntegerField()
    allergens = models.ManyToManyField(Allergen, help_text='Select an allergen contained in this ingredient')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
'''

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
    nutritional_info = models.TextField(blank=True)
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

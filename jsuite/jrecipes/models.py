from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Allergen(models.Model):
    type = models.CharField(max_length=150) # Nuts, Lactose, etc...

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.type
    

class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    calories = models.IntegerField()
    allergens = models.ManyToManyField(Allergen, help_text='Select an allergen contained in this ingredient')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    categories = models.ManyToManyField(Categorie, help_text='Select a categorie for this recipe')
    portion_size = models.IntegerField()
    prep_time = models.IntegerField()  # In minutes
    cook_time = models.IntegerField()  # In minutes
    ingredients = models.ManyToManyField(Ingredient, help_text='Select an ingredient for this recipe')
    instructions = models.TextField()
    additional_notes = models.TextField()
    nutritional_info = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    #def calculateCalories(self):
    #    for x in self.ingredients.get_queryset():
    #        caloriesCount += x.calories
    #    return caloriesCount

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

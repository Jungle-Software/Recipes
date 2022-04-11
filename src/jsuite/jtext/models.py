from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    portion_size = models.IntegerField()
    prep_time = models.IntegerField()  # In minutes
    cook_time = models.IntegerField()  # In minutes
    ingredients = models.TextField()
    instructions = models.TextField()
    additional_notes = models.TextField()
    nutritional_info = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

from django.contrib import admin

from .models import Recipe
from .models import Ingredient
from .models import Allergen
from .models import Categorie

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Allergen)
admin.site.register(Categorie)

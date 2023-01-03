from django.contrib import admin

from .models import Category
from .models import Allergen
from .models import InstructionStep
from .models import Ingredient
from .models import IngredientListItem
from .models import Recipe

admin.site.register(Category)
admin.site.register(Allergen)
admin.site.register(InstructionStep)
admin.site.register(Ingredient)
admin.site.register(IngredientListItem)
admin.site.register(Recipe)


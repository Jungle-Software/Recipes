from django.contrib import admin

from .models import Recipe
from .models import Allergen
from .models import Category
from .models import NutritionalUnit
from .models import NutritionalInfo

admin.site.register(Recipe)
admin.site.register(Allergen)
admin.site.register(Category)
admin.site.register(NutritionalUnit)
admin.site.register(NutritionalInfo)


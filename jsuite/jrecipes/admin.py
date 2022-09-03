from django.contrib import admin

from .models import Recipe
from .models import Allergen
from .models import Category

admin.site.register(Recipe)
admin.site.register(Allergen)
admin.site.register(Category)

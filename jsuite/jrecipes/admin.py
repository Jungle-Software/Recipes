from django.contrib import admin

from .models import Recipe
from .models import Allergen
from .models import Category
from .models import NutritionalInfo
from .models import InstructionStep
from .models import Instruction

admin.site.register(Recipe)
admin.site.register(Allergen)
admin.site.register(Category)
admin.site.register(NutritionalInfo)
admin.site.register(InstructionStep)
admin.site.register(Instruction)


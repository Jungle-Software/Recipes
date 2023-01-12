from django.contrib import admin

from .models import Category, Allergen, InstructionStep, InstructionSubStep, Ingredient, IngredientListItem, Recipe

class InstructionStepInline(admin.TabularInline):
    model = InstructionStep

class InstructionSubStepInline(admin.TabularInline):
    model = InstructionSubStep

class InstructionStepAdmin(admin.ModelAdmin):
    inlines = [InstructionSubStepInline]

class IngredientListItemInline(admin.TabularInline):
    model = IngredientListItem

class RecipeAdmin(admin.ModelAdmin):
    inlines = [InstructionStepInline, IngredientListItemInline]

admin.site.register(Category)
admin.site.register(Allergen)
admin.site.register(InstructionStep, InstructionStepAdmin)
admin.site.register(InstructionSubStep)
admin.site.register(Ingredient)
admin.site.register(IngredientListItem)
admin.site.register(Recipe, RecipeAdmin)



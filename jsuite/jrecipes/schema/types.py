import graphene
from graphene_django import DjangoObjectType

from ..models import Recipe, Category, Allergen


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class CategoryInput(graphene.InputObjectType):
    name = graphene.String()


class AllergenType(DjangoObjectType):
    class Meta:
        model = Allergen
        fields = (
            'id',
            'type',
        )


class AllergenInput(graphene.InputObjectType):
    type = graphene.String()

'''
class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'calories',
            'allergens',
        )


class IngredientInput(graphene.InputObjectType):
    name = graphene.String()
    calories = graphene.Int()
    allergen = graphene.Field(AllergenInput)
'''

class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'description',
            'categories',
            'portion_size',
            'prep_time',
            'cook_time',
            'ingredients',
            'allergens',
            'instructions',
            'additional_notes',
            'nutritional_info',
            'parentSubRecipe',
            'date_created',
        )


class RecipeInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
    categories = graphene.Field(CategoryInput)
    portion_size = graphene.Int()
    prep_time = graphene.Int()
    cook_time = graphene.Int()
    ingredients = graphene.Field(lambda: RecipeInput)
    allergens = graphene.Field(AllergenInput)
    instructions = graphene.String()
    additional_notes = graphene.String()
    nutritional_info = graphene.String()
    parentSubRecipe = graphene.Int()


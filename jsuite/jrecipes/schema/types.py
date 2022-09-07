import graphene
from graphene_django import DjangoObjectType

from ..models import Recipe, Category, Allergen, NutritionalUnit, NutritionalInfo


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

class NutritionalUnitType(DjangoObjectType):
    class Meta:
        model = NutritionalUnit
        fields = (
            'id',
            'serving_size',
            'unit',
        )

class NutritionalUnitInput(graphene.InputObjectType):
    serving_size = graphene.Int()
    unit = graphene.Int()   # Change to Enum when you figure out how

class NutritionalInfoType(DjangoObjectType):
    class Meta:
        model = NutritionalInfo
        fields = (
            'id',
            'nutritional_unit',
            'calories',
        )

class NutritionalInfoInput(graphene.InputObjectType):
    nutritional_unit = graphene.Field(NutritionalUnitInput)
    calories = graphene.Int()

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
    portion_size = graphene.Int()  # TODO rename to servings
    prep_time = graphene.Int()
    cook_time = graphene.Int()
    ingredients = graphene.Field(lambda: RecipeInput)
    allergens = graphene.Field(AllergenInput)
    instructions = graphene.String()  # TODO make instructions object (which contains step objects (one photo + string))
    type_enum = graphene.Int()  # TODO make it an enum and change elsewhere (remove parentSubRecipe): 0 = recipe, 1 = recipe that can be used as an ingredient (sauce, bread etc) 2 = ingredient
    # TODO remove all unused comments (ingredients)
    # TODO add thumbnail
    # TODO add nutritional info
    
'''
TODO add nutritional info

portion size (number, unit) [another separate object - many to one]
calories

everything that is on a label
''' 
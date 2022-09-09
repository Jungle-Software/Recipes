import graphene
from graphene_django import DjangoObjectType

from ..models import Recipe, Category, Allergen, NutritionalInfo


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


class NutritionalInfoType(DjangoObjectType):
    class Meta:
        model = NutritionalInfo
        fields = (
            'id',
            'quantity',
            'unit',
            'calories',
        )


class NutritionalInfoInput(graphene.InputObjectType):
    quantity = graphene.Int()
    unit = graphene.Enum.from_enum(NutritionalInfo.UnitType)
    calories = graphene.Int()


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'description',
            'categories',
            'servings',
            'prep_time',
            'cook_time',
            'ingredients',
            'allergens',
            'instructions',
            'additional_notes',
            'nutritional_info',
            'type_enum',
            'date_created',
        )


class RecipeInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
    categories = graphene.Field(CategoryInput)
    servings = graphene.Int()
    prep_time = graphene.Int()
    cook_time = graphene.Int()
    ingredients = graphene.Field(lambda: RecipeInput)
    allergens = graphene.Field(AllergenInput)
    instructions = graphene.String()  # TODO make instructions object (which contains step objects (one photo + string))
    type_enum = graphene.Enum.from_enum(Recipe.TypeEnum)
    # TODO add thumbnail
    nutritional_info = graphene.Field(NutritionalInfoInput)
    
'''
TODO add nutritional info **PARTLY  DONE**

portion size (number, unit) [another separate object - many to one]
calories

everything that is on a label
''' 
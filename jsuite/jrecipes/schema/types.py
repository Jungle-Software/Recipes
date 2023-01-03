import graphene
from graphene_django import DjangoObjectType

from ..models import Category, Allergen, InstructionStep, Ingredient, IngredientListItem, Recipe


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

class InstructionStepType(DjangoObjectType):
    class Meta:
        model = InstructionStep
        fields = (
            'id',
            'text',
            #'image',
            'sub_steps',
        )

class InstructionStepInput(graphene.InputObjectType):
    #image = graphene.String() # TODO FIX THIS!!
    text = graphene.String()
    sub_steps = graphene.Field(lambda: InstructionStepInput)

'''
class InstructionType(DjangoObjectType):
    class Meta:
        model = Instruction
        fields = (
            'id',
            'instruction_steps',
        )

class InstructionInput(graphene.InputObjectType):
    instruction_steps = graphene.Field(InstructionStepInput)

'''

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'allergen',
        )

class IngredientInput(graphene.InputObjectType):
    name = graphene.String()
    allergen = graphene.Field(AllergenInput)


class IngredientListItemType(DjangoObjectType):
    class Meta:
        model = IngredientListItem
        fields = (
            'id',
            'ingredient'
            'unit',
            'quantity',
        )

class IngredientListItemInput(graphene.InputObjectType):
    ingredient = graphene.Field(IngredientInput)
    unit = graphene.Enum.from_enum(IngredientListItem.unit)
    quantity = graphene.Decimal()

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
            'ingredient_list',
            'allergens',
            'instructions',
            'additional_notes',
            'date_updated',
            'date_created',
        )


class RecipeInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
    categories = graphene.Field(CategoryInput)
    servings = graphene.Int()
    prep_time = graphene.Int()
    cook_time = graphene.Int()
    ingredient_list = graphene.Field(IngredientListItemInput)
    allergens = graphene.Field(AllergenInput)
    instructions = graphene.Field(InstructionStepInput)
    # TODO add thumbnail

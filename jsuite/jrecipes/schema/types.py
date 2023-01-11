import graphene
from graphene_django import DjangoObjectType

from ..models import Category, Allergen, InstructionStep, InstructionSubStep, Ingredient, IngredientListItem, UnitType, Recipe

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )

class AllergenType(DjangoObjectType):
    class Meta:
        model = Allergen
        fields = (
            'id',
            'type',
        )

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'allergens',
        )

class IngredientListItemType(DjangoObjectType):
    class Meta:
        model = IngredientListItem
        fields = (
            'id',
            'recipe',
            'ingredient',
            'unit',
            'quantity',
        )

    ingredient = graphene.List(IngredientType)

    @staticmethod
    def resolve_ingredient(parent, info):
        return Ingredient.objects.filter(ingredient_list_item=parent)

class InstructionSubStepType(DjangoObjectType):
    class Meta:
        model = InstructionSubStep
        fields = (
            'id',
            'step',
            'text'
            #'image',
        )

class InstructionStepType(DjangoObjectType):
    class Meta:
        model = InstructionStep
        fields = (
            'id',
            'recipe',
            'sub_instructions',
            'title',
            'text'
            #'image',
        )

    sub_instructions = graphene.List(InstructionSubStepType)

    @staticmethod
    def resolve_sub_instructions(parent, info):
        return InstructionSubStep.objects.filter(step=parent)

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
            'allergens',
            'instructions',
            'ingredients',
            'additional_notes',
            'date_updated',
            'date_created',
        )

    instructions = graphene.List(InstructionStepType)
    ingredients = graphene.List(IngredientListItemType)

    @staticmethod
    def resolve_instructions(parent, info):
        return InstructionStep.objects.filter(recipe=parent)

    @staticmethod
    def resolve_ingredients(parent, info):
        return IngredientListItem.objects.filter(recipe=parent)


class CategoryInput(graphene.InputObjectType):
    name = graphene.String()

class AllergenInput(graphene.InputObjectType):
    type = graphene.String()

class RecipeInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
    categories = graphene.Field(CategoryInput)
    servings = graphene.Int()
    prep_time = graphene.Int()
    cook_time = graphene.Int()
    allergens = graphene.Field(AllergenInput)
    additional_notes = graphene.String()
    # TODO add thumbnail

class InstructionStepInput(graphene.InputObjectType):
    recipe = graphene.Field(RecipeInput)
    title = graphene.String()
    text = graphene.String()
    #image = graphene.String() # TODO FIX THIS!!

class InstructionSubStepInput(graphene.InputObjectType):
    step = graphene.Field(InstructionStepInput)
    text = graphene.String()

class IngredientListItemInput(graphene.InputObjectType):
    recipe = graphene.Field(RecipeInput)
    unit = graphene.Enum.from_enum(UnitType)
    quantity = graphene.Decimal()

class IngredientInput(graphene.InputObjectType):
    ingredient_list = graphene.Field(IngredientListItemInput)
    name = graphene.String()
    allergen = graphene.Field(AllergenInput)



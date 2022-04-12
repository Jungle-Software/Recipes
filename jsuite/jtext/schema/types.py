import graphene
from graphene_django import DjangoObjectType

from ..models import Recipe


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'description',
            'portion_size',
            'prep_time',
            'cook_time',
            'ingredients',
            'instructions',
            'additional_notes',
            'nutritional_info',
            'date_created',
        )


class RecipeInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
    portion_size = graphene.Int()
    prep_time = graphene.Int()
    cook_time = graphene.Int()
    ingredients = graphene.String()
    instructions = graphene.String()
    additional_notes = graphene.String()
    nutritional_info = graphene.String()

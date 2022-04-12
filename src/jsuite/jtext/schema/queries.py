import graphene

from ..models import Recipe
from .types import RecipeType


class Query(graphene.ObjectType):
    recipes = graphene.List(RecipeType)

    def resolve_recipes(root, info, **kwargs):
        # Querying a list
        return Recipe.objects.all()

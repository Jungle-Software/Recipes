import graphene

from ..models import Recipe
from .types import RecipeType


class Query(graphene.ObjectType):
    all_recipes = graphene.List(RecipeType)
    recipe_by_id = graphene.Field(RecipeType, id=graphene.Int())

    # Querying a list
    def resolve_all_recipes(root, info, **kwargs):
        return Recipe.objects.all()

    # Querying a single recipe
    def resolve_recipe_by_id(root, info, id):
        # In the front-end, we use default id = 0 until the user selects a recipe
        if id == 0:
            return None
        return Recipe.objects.get(pk=id)



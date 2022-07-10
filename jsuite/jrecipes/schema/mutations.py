import graphene

from jrecipes.models import Recipe
from jrecipes.schema.types import RecipeInput, RecipeType


class CreateRecipe(graphene.Mutation):
    class Arguments:
        input = RecipeInput(required=True)

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, root, info, input):
        recipe = Recipe()
        recipe.title = input.title
        recipe.description = input.description
        recipe.portion_size = input.portion_size
        recipe.prep_time = input.prep_time
        recipe.cook_time = input.cook_time
        recipe.ingredients = input.ingredients
        recipe.instructions = input.instructions
        recipe.additional_notes = input.additional_notes
        recipe.nutritional_info = input.nutritional_info

        recipe.save()
        return CreateRecipe(recipe=recipe)


class UpdateRecipe(graphene.Mutation):
    class Arguments:
        input = RecipeInput(required=True)
        id = graphene.ID()

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, root, info, input, id):
        recipe = Recipe.objects.get(pk=id)
        recipe.title = input.title
        recipe.description = input.description
        recipe.portion_size = input.portion_size
        recipe.prep_time = input.prep_time
        recipe.cook_time = input.cook_time
        recipe.ingredients = input.ingredients
        recipe.instructions = input.instructions
        recipe.additional_notes = input.additional_notes
        recipe.nutritional_info = input.nutritional_info
        recipe.save()
        return UpdateRecipe(recipe=recipe)


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()

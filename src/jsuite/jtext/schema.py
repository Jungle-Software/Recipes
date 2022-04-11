import graphene
from graphene_django import DjangoObjectType
from .models import Recipe


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


class Query(graphene.ObjectType):
    recipes = graphene.List(RecipeType)

    def resolve_recipes(root, info, **kwargs):
        # Querying a list
        return Recipe.objects.all()
    
    
class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

import graphene

from jrecipes.models import Recipe, Category, Allergen
from jrecipes.schema.types import RecipeInput, RecipeType, CategoryInput, CategoryType, AllergenInput, AllergenType


class CreateAllergen(graphene.Mutation):
    class Arguments:
        input = AllergenInput(required=True)

    allergen = graphene.Field(AllergenType)

    @classmethod
    def mutate(cls, root, info, input):
        allergen = Allergen()
        allergen.type = input.type

        allergen.save()
        return CreateAllergen(allergen=allergen)


class UpdateAllergen(graphene.Mutation):
    class Arguments:
        input = AllergenInput(required=True)
        id = graphene.ID()

    allergen = graphene.Field(AllergenType)

    @classmethod
    def mutate(cls, root, info, input, id):
        allergen = Allergen.objects.get(pk=id)
        allergen.type = input.type
        allergen.save()
        return UpdateAllergen(allergen=allergen)

class DeleteAllergen(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    allergen = graphene.Field(AllergenType)

    @classmethod
    def mutate(cls, root, info, id):
        allergen = Allergen.objects.get(pk=id)
        allergen.delete()
        return


class CreateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, input):
        category = Category()
        category.name = input.name

        category.save()
        return CreateCategory(category=category)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, input, id):
        category = Category.objects.get(pk=id)
        category.name = input.name
        category.save()
        return UpdateCategory(category=category)

class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(pk=id)
        category.delete()
        return


class CreateRecipe(graphene.Mutation):
    class Arguments:
        input = RecipeInput(required=True)

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, root, info, input):
        recipe = Recipe()
        recipe.title = input.title
        recipe.description = input.description
        recipe.categories = input.categories
        recipe.servings = input.servings
        recipe.prep_time = input.prep_time
        recipe.cook_time = input.cook_time
        recipe.ingredients = input.ingredients
        recipe.allergens = input.allergens
        recipe.instructions = input.instructions
        recipe.additional_notes = input.additional_notes
        recipe.nutritional_info = input.nutritional_info
        recipe.parentSubRecipe = input.parentSubRecipe

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
        recipe.categories = input.categories
        recipe.servings = input.servings
        recipe.prep_time = input.prep_time
        recipe.cook_time = input.cook_time
        recipe.ingredients = input.ingredients
        recipe.allergens = input.allergens
        recipe.instructions = input.instructions
        recipe.additional_notes = input.additional_notes
        recipe.nutritional_info = input.nutritional_info
        recipe.parentSubRecipe = input.nutritional_info
        recipe.save()
        return UpdateRecipe(recipe=recipe)

class DeleteRecipe(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    recipe = graphene.Field(RecipeType)

    @classmethod
    def mutate(cls, root, info, id):
        recipe = Recipe.objects.get(pk=id)
        recipe.delete()
        return

class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()
    delete_recipe = DeleteRecipe.Field()
    
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_allergen = CreateAllergen.Field()
    update_allergen = UpdateAllergen.Field()
    delete_allergen = DeleteAllergen.Field()
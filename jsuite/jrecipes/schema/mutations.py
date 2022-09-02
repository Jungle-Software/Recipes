import graphene

from jrecipes.models import Recipe, Category, Ingredient, Allergen
from jrecipes.schema.types import RecipeInput, RecipeType, CategoryInput, CategoryType, IngredientInput, IngredientType, AllergenInput, AllergenType


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


class CreateIngredient(graphene.Mutation):
    class Arguments:
        input = IngredientInput(required=True)

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, input):
        ingredient = Ingredient()
        ingredient.name = input.name
        ingredient.calories = input.calories
        ingredient.allergens = input.allergens

        ingredient.save()
        return CreateIngredient(ingredient=ingredient)


class UpdateIngredient(graphene.Mutation):
    class Arguments:
        input = IngredientInput(required=True)
        id = graphene.ID()

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, input, id):
        ingredient = Ingredient.objects.get(pk=id)
        ingredient.name = input.name
        ingredient.calories = input.calories
        ingredient.allergens = input.allergens
        ingredient.save()
        return UpdateIngredient(ingredient=ingredient)


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
        recipe.categories = input.categories
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

    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()

    create_allergen = CreateAllergen.Field()
    update_allergen = UpdateAllergen.Field()

    create_ingredient = CreateIngredient.Field()
    update_ingredient = UpdateIngredient.Field()
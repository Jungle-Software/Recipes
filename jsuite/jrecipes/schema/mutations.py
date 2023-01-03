import graphene

from jrecipes.models import Category, Allergen, InstructionStep, Ingredient, IngredientListItem, Recipe
from jrecipes.schema.types import CategoryInput, CategoryType, AllergenInput, AllergenType, InstructionStepInput, InstructionStepType, IngredientInput, IngredientType, IngredientListItemInput, IngredientListItemType, RecipeInput, RecipeType


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

class CreateInstructionStep(graphene.Mutation):
    class Arguments:
        input = InstructionStepInput(required=True)

    instruction_step = graphene.Field(InstructionStepType)

    @classmethod
    def mutate(cls, root, info, input):
        instruction_step = InstructionStep()
        instruction_step.text = input.text
        instruction_step.sub_steps = input.sub_steps

        instruction_step.save()
        return CreateInstructionStep(instruction_step=instruction_step)

class UpdateInstructionStep(graphene.Mutation):
    class Arguments:
        input = InstructionStepInput(required=True)
        id = graphene.ID()

    instruction_step = graphene.Field(InstructionStepType)

    @classmethod
    def mutate(cls, root, info, input, id):
        instruction_step = InstructionStep.objects.get(pk=id)
        instruction_step.text = input.text
        instruction_step.sub_steps = input.sub_steps
        instruction_step.save()
        return UpdateInstructionStep(instruction_step=instruction_step)

class DeleteInstructionStep(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    instruction_step = graphene.Field(InstructionStepType)

    @classmethod
    def mutate(cls, root, info, id):
        instruction_step = InstructionStep.objects.get(pk=id)
        instruction_step.delete()
        return

class CreateIngredient(graphene.Mutation):
    class Arguments:
        input = IngredientInput(required=True)

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, input):
        ingredient = IngredientInput()
        ingredient.name = input.name
        ingredient.allergen = input.allergen

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
        ingredient.allergen = input.allergen
        ingredient.save()
        return UpdateIngredient(ingredient=ingredient)

class DeleteIngredient(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, id):
        ingredient = Ingredient.objects.get(pk=id)
        ingredient.delete()
        return

class CreateIngredientListItem(graphene.Mutation):
    class Arguments:
        input = IngredientListItemInput(required=True)

    ingredient_list_item = graphene.Field(IngredientListItemType)

    @classmethod
    def mutate(cls, root, info, input):
        ingredient_list_item = IngredientListItemInput()
        ingredient_list_item.ingredient = input.ingredient
        ingredient_list_item.unit = input.unit
        ingredient_list_item.quantity = input.quantity

        ingredient_list_item.save()
        return CreateIngredientListItem(ingredient_list_item=ingredient_list_item)

class UpdateIngredientListItem(graphene.Mutation):
    class Arguments:
        input = IngredientListItemInput(required=True)
        id = graphene.ID()

    ingredient_list_item = graphene.Field(IngredientListItemType)

    @classmethod
    def mutate(cls, root, info, input, id):
        ingredient_list_item = IngredientListItem.objects.get(pk=id)
        ingredient_list_item.ingredient = input.ingredient
        ingredient_list_item.unit = input.unit
        ingredient_list_item.quantity = input.quantity
        ingredient_list_item.save()
        return UpdateIngredientListItem(ingredient_list_item=ingredient_list_item)

class DeleteIngredientListItem(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ingredient_list_item = graphene.Field(IngredientListItemType)

    @classmethod
    def mutate(cls, root, info, id):
        ingredient_list_item = IngredientListItem.objects.get(pk=id)
        ingredient_list_item.delete()
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
        recipe.ingredient_list = input.ingredient_list
        recipe.allergens = input.allergens
        recipe.instructions = input.instructions
        recipe.additional_notes = input.additional_notes

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
        recipe.ingredient_list = input.ingredient_list
        recipe.allergens = input.allergens
        recipe.instructions = input.instructions
        recipe.additional_notes = input.additional_notes
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
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_allergen = CreateAllergen.Field()
    update_allergen = UpdateAllergen.Field()
    delete_allergen = DeleteAllergen.Field()

    create_instruction_step = CreateInstructionStep.Field()
    update_instruction_step = UpdateInstructionStep.Field()
    delete_instruction_step = DeleteInstructionStep.Field()

    create_ingredient = CreateIngredient.Field()
    update_ingredient = UpdateIngredient.Field()
    delete_ingredient = DeleteIngredient.Field()

    create_ingredient_list_item = CreateIngredientListItem.Field()
    update_ingredient_list_item = UpdateIngredientListItem.Field()
    delete_ingredient_list_item = DeleteIngredientListItem.Field()

    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()
    delete_recipe = DeleteRecipe.Field()



import datetime

from ..models import Category, Allergen, InstructionStep, InstructionSubStep, Ingredient, IngredientListItem, Recipe


def insert_data():
    #TEST 1
    categoryTest1 = Category.objects.create(
        name="CategoryTest1"
    )

    allergenTest1 = Allergen.objects.create(
        type="AllergenTypeTest1"
    )

    recipeTest1 = Recipe.objects.create(
        title="Test1",
        description="My first test!",
        servings=4,
        prep_time=20,
        cook_time=40,
        additional_notes="Pretty tasty",
    )
    recipeTest1.categories.add(categoryTest1)
    recipeTest1.allergens.add(allergenTest1)

    instructionTest1 = InstructionStep.objects.create(
        recipe=recipeTest1,
        title="TitleTest1",
        text="InstructionStepTest1"
    )

    instructionSubStepTest1 = InstructionSubStep.objects.create(
        step=instructionTest1,
        text="InstructionSubStepTest1",
    )

    ingredientTest1 = Ingredient.objects.create(
        name="IngredientNameTest1",
    )
    ingredientTest1.allergens.add(allergenTest1)

    ingredientListItemTest1 = IngredientListItem.objects.create(
        recipe=recipeTest1,
        ingredient=ingredientTest1,
        unit="gram",
        quantity="300"
    )

    #TEST 2
    categoryTest2 = Category.objects.create(
        name="CategoryTest2"
    )

    allergenTest2 = Allergen.objects.create(
        type="AllergenTypeTest2"
    )

    recipeTest2 = Recipe.objects.create(
        title="Test2",
        description="My first test!",
        servings=4,
        prep_time=20,
        cook_time=40,
        additional_notes="Pretty tasty",
    )
    recipeTest2.categories.add(categoryTest2)
    recipeTest2.allergens.add(allergenTest2)

    instructionTest2 = InstructionStep.objects.create(
        recipe=recipeTest2,
        title="TitleTest2",
        text="InstructionStepTest2"
    )

    instructionSubStepTest2 = InstructionSubStep.objects.create(
        step=instructionTest2,
        text="InstructionSubStepTest2",
    )

    ingredientTest2 = Ingredient.objects.create(
        name="IngredientNameTest2",
    )
    ingredientTest2.allergens.add(allergenTest2)

    ingredientListItemTest2 = IngredientListItem.objects.create(
        recipe=recipeTest2,
        ingredient=ingredientTest2,
        unit="gram",
        quantity="300"
    )

    # Overriding creation date for snapshot testing
    Recipe.objects.filter(title="Test1").update(date_created=datetime.date(2022, 5, 5))
    Recipe.objects.filter(title="Test2").update(date_created=datetime.date(2022, 5, 5))
    Recipe.objects.filter(title="Test1").update(date_updated=datetime.date(2022, 5, 5))
    Recipe.objects.filter(title="Test2").update(date_updated=datetime.date(2022, 5, 5))










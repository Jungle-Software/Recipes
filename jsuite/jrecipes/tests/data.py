import datetime

from ..models import Category, Allergen, InstructionStep, Ingredient, IngredientListItem, Recipe


def insert_data():
    #TEST 1
    categoryTest1 = Category.objects.create(
        name="CategoryTest1"
    )

    allergenTest1 = Allergen.objects.create(
        type="AllergenTypeTest1"
    )

    sub_instructionTest1 = InstructionStep.objects.create(
        text="SubInstructionStepTest1"
    )

    instructionTest1 = InstructionStep.objects.create(
        text="InstructionStepTest1"
    )
    instructionTest1.sub_steps.add(sub_instructionTest1)

    ingredientTest1 = Ingredient.objects.create(
        name="IngredientNameTest1"
    )
    ingredientTest1.allergens.add(allergenTest1)

    ingredientListItemTest1 = IngredientListItem.objects.create(
        ingredient=ingredientTest1,
        unit="gram",
        quantity="300"
    )
    #ingredientListItemTest1.ingredient.add(ingredientTest1)

    recipeTest1 = Recipe.objects.create(
        title="Test1",
        description="My first test!",
        servings=4,
        prep_time=20,
        cook_time=40,
        instructions=instructionTest1,
        additional_notes="Pretty tasty",
    )
    recipeTest1.categories.add(categoryTest1)
    recipeTest1.ingredient_list.add(ingredientListItemTest1)
    #recipeTest1.instructions.add(instructionTest1)

    #TEST 2
    categoryTest2 = Category.objects.create(
        name="CategoryTest2"
    )

    allergenTest2 = Allergen.objects.create(
        type="AllergenTypeTest2"
    )

    sub_instructionTest2 = InstructionStep.objects.create(
        text="SubInstructionStepTest2"
    )

    instructionTest2 = InstructionStep.objects.create(
        text="InstructionStepTest2",
    )

    instructionTest2.sub_steps.add(sub_instructionTest2)

    ingredientTest2 = Ingredient.objects.create(
        name="IngredientNameTest2"
    )
    ingredientTest2.allergens.add(allergenTest2)

    ingredientListItemTest2 = IngredientListItem.objects.create(
        ingredient=ingredientTest2,
        unit="gram",
        quantity="600"
    )
    #ingredientListItemTest2.ingredient.add(ingredientTest2)

    recipeTest2 = Recipe.objects.create(
        title="Test2",
        description="My second test!",
        servings=6,
        prep_time=30,
        cook_time=60,
        instructions=instructionTest2,
        additional_notes="Not Tasty"
    )
    recipeTest2.categories.add(categoryTest2)
    recipeTest2.ingredient_list.add(ingredientListItemTest2)
    #recipeTest2.instructions.add(instructionTest2)

    # Overriding creation date for snapshot testing
    Recipe.objects.filter(title="Test1").update(date_created=datetime.date(2022, 5, 5))
    Recipe.objects.filter(title="Test2").update(date_created=datetime.date(2022, 5, 5))
    Recipe.objects.filter(title="Test1").update(date_updated=datetime.date(2022, 5, 5))
    Recipe.objects.filter(title="Test2").update(date_updated=datetime.date(2022, 5, 5))

    '''
    #Test 2
    categoryTest2 = Category.objects.create(
        name="CategoryTest2"
    )

    allergenTest2 = Allergen.objects.create(
        type="AllergenTypeTest2"
    )

    ingredientTest2 = Ingredient.objects.create(
        name="IngredientNameTest2",
        calories=300,
    )
    ingredientTest2.allergens.add(allergenTest2)

    recipeTest2 = Recipe.objects.create(
        title="Testerino 2",
        description="The second :^)",
        portion_size=4,
        prep_time=20,
        cook_time=40,
        instructions="Do this, then that.",
        additional_notes="Greasy af",
        nutritional_info="None"
    )
    recipeTest2.categories.add(categoryTest2)
    recipeTest2.ingredients.add(ingredientTest2)
    '''









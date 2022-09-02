import datetime

from ..models import Recipe, Category, Ingredient, Allergen


def insert_data():
    #TEST 1
    categoryTest1 = Category.objects.create(
        name="CategoryTest1"
    )

    allergenTest1 = Allergen.objects.create(
        type="AllergenTypeTest1"
    )

    ingredientTest1 = Ingredient.objects.create(
        name="IngredientNameTest1",
        calories=150,
    )
    ingredientTest1.allergens.add(allergenTest1)

    recipeTest1 = Recipe.objects.create(
        title="Test1",
        description="My first test!",
        portion_size=4,
        prep_time=20,
        cook_time=40,
        instructions="Do this, then that.",
        additional_notes="Pretty tasty",
        nutritional_info="Pretty healthy"
    )
    recipeTest1.categories.add(categoryTest1)
    recipeTest1.ingredients.add(ingredientTest1)

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

    # Overriding creation date for snapshot testing
    Recipe.objects.filter(title="Test1").update(date_created=datetime.date(2022, 5, 5))
    Recipe.objects.filter(title="Testerino 2").update(date_created=datetime.date(2022, 5, 5))


from graphene.test import Client
from snapshottest.django import TestCase
from jrecipes.schema.schema import schema
from .data import insert_data
from ..models import Recipe


class RecipesQueryTestCase(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.maxDiff = None
        insert_data()

    def test_all_recipes(self):
        response = self.client.execute("""
            query {
              allRecipes {
                id
                title
              }
            }
        """)
        self.assertMatchSnapshot(response)

    def test_recipe_by_id(self):
        # Manually get the id of the specific entry, because it will not always be the same
        entry_id = Recipe.objects.filter(title="Test1")[0].id
        response = self.client.execute("""
          query RecipeView($id: Int!) {
            recipeById (id: $id) {
              title
              description
              portionSize
              prepTime
              cookTime
              ingredients
              instructions
              additionalNotes
              nutritionalInfo
              dateCreated
            }
          }
        """, variables={"id": entry_id})
        self.assertMatchSnapshot(response)




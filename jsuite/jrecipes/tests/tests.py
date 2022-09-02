from graphene.test import Client
from snapshottest.django import TestCase
from jrecipes.schema.schema import schema
from .data import insert_data
from ..models import Recipe


# TODO Do NOT forget to reset the backend test coverage in .coveragerc back to 90% once this task is done, because by then the mutations should be fully tested.
class RecipesTestCase(TestCase):
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
          query RecipeView($id: ID!) {
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

    def test_delete_recipe(self):
        entry_id = Recipe.objects.filter(title="Test1")[0].id
        response = self.client.execute("""
            mutation DeleteRecipe($id: ID!) {
                    deleteRecipe (id: $id) {
                        recipe {
                        id
                    }
                }
            }
        """, variables={"id": entry_id})
        self.assertMatchSnapshot(response)



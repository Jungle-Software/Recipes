from graphene.test import Client
from snapshottest.django import TestCase
from jrecipes.schema.schema import schema
from .data import insert_data


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
        """, variables={"id": 1})
        self.assertMatchSnapshot(response)




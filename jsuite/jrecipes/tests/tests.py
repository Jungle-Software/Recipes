from graphene.test import Client
from snapshottest.django import TestCase
from jrecipes.schema.schema import schema
from ..models import Recipe


class RecipesTestCase(TestCase):
    fixtures = ["../tests/test_fixtures/jrecipes.json"]

    def setUp(self):
        self.client = Client(schema)
        self.maxDiff = None

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
            query RecipeView($id: ID!) {
                recipeById (id: $id) {
                    title
                    description
                    categories{
                      name
                    }
                    servings
                    prepTime
                    cookTime
                    instructions{
                      title
                      text
                      subInstructions {
                        text
                      }
                    }
                    ingredients{
                      ingredient{
                        name
                        allergens{
                            type
                        }
                      }
                      unit
                      quantity
                    }
                    additionalNotes
                    dateUpdated
                    dateCreated
                }
            }
        """, variables={"id": 1})  # Using direct ID, matching the pk determined in the fixture for these tests
        self.assertMatchSnapshot(response)

    def test_delete_recipe(self):
        response = self.client.execute("""
            mutation DeleteRecipe($id: ID!) {
                    deleteRecipe (id: $id) {
                        recipe {
                        id
                    }
                }
            }
        """, variables={"id": 2})  # Using direct ID, matching the pk determined in the fixture for these tests
        self.assertMatchSnapshot(response)



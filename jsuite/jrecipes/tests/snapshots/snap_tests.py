# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['RecipesTestCase::test_all_recipes 1'] = {
    'data': {
        'allRecipes': [
            {
                'id': '1',
                'title': 'Test1'
            },
            {
                'id': '2',
                'title': 'Test2'
            }
        ]
    }
}

snapshots['RecipesTestCase::test_delete_recipe 1'] = {
    'data': {
        'deleteRecipe': None
    }
}

snapshots['RecipesTestCase::test_recipe_by_id 1'] = {
    'data': {
        'recipeById': {
            'additionalNotes': 'Pretty tasty',
            'categories': [
                {
                    'name': 'CategoryTest1'
                }
            ],
            'cookTime': 40,
            'dateCreated': '2022-05-05',
            'dateUpdated': '2022-05-05',
            'description': 'My first test!',
            'ingredientList': [
                {
                    'ingredient': {
                        'allergens': [
                            {
                                'type': 'AllergenTypeTest1'
                            }
                        ],
                        'name': 'IngredientNameTest1'
                    }
                }
            ],
            'instructions': {
                'subSteps': [
                    {
                        'text': 'SubInstructionStepTest1'
                    }
                ],
                'text': 'InstructionStepTest1'
            },
            'prepTime': 20,
            'servings': 4,
            'title': 'Test1'
        }
    }
}

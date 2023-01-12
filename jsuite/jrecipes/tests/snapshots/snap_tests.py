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
                'title': 'Test Recipe 1'
            },
            {
                'id': '2',
                'title': 'Test Recipe 2'
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
            'additionalNotes': '',
            'categories': [
                {
                    'name': 'Vegan'
                }
            ],
            'cookTime': 3,
            'dateCreated': '2023-01-11',
            'dateUpdated': '2023-01-11',
            'description': 'This is the first recipe used for testing.',
            'ingredients': [
                {
                    'ingredient': [
                        {
                            'allergens': [
                            ],
                            'name': 'Test Ingredient 2'
                        }
                    ],
                    'quantity': '1.5000',
                    'unit': 'CUP'
                },
                {
                    'ingredient': [
                        {
                            'allergens': [
                                {
                                    'type': 'Test Allergen 1'
                                }
                            ],
                            'name': 'Test Ingredient 1'
                        }
                    ],
                    'quantity': '3.0000',
                    'unit': 'UNIT'
                }
            ],
            'instructions': [
                {
                    'subInstructions': [
                        {
                            'text': 'Substep 1 is to read this substep.'
                        },
                        {
                            'text': 'Substep 2 is to inevitably skip this substep and hope no error was thrown in testing.'
                        }
                    ],
                    'text': 'In this step, we will perform all the following substeps',
                    'title': 'First Step'
                },
                {
                    'subInstructions': [
                    ],
                    'text': 'This step has no substeps',
                    'title': 'Second Step'
                }
            ],
            'prepTime': 2,
            'servings': 1,
            'title': 'Test Recipe 1'
        }
    }
}

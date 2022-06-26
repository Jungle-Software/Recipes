# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['RecipesQueryTestCase::test_all_recipes 1'] = {
    'data': {
        'allRecipes': [
            {
                'id': '1',
                'title': 'Test1'
            },
            {
                'id': '2',
                'title': 'Testerino 2'
            }
        ]
    }
}

snapshots['RecipesQueryTestCase::test_recipe_by_id 1'] = {
    'data': {
        'recipeById': {
            'additionalNotes': 'Pretty tasty',
            'cookTime': 40,
            'dateCreated': '2022-05-05',
            'description': 'My first test!',
            'ingredients': 'This will be changed!!',
            'instructions': 'Do this, then that.',
            'nutritionalInfo': 'Pretty healthy',
            'portionSize': 4,
            'prepTime': 20,
            'title': 'Test1'
        }
    }
}

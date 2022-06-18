import { hasOperationName } from '../utils/graphql-test-utils'

describe('recipe page', () => {
    const recipeApiUrl = Cypress.env('apiUrl') + '/recipes';
    console.log(recipeApiUrl+ "7f5tgyvhbjju7yhgtbhvjk678%EDRTFGVHo");

    beforeEach(() => {
        cy.intercept('POST', recipeApiUrl, (req) => {
            if (hasOperationName(req, 'AllRecipes')) {
                req.alias = 'AllRecipesResponse'
                req.reply({ fixture: 'Recipes/allRecipes'})
            }

            if (hasOperationName(req, 'RecipeById')) {
                req.alias = 'RecipeByIdResponse'
                req.reply({ fixture: 'Recipes/recipeById'})
            }
        })
    })

    it('prompts the user to select a recipe', () => {
        cy.visit('/recipes')
        cy.get('[id=select-recipe-prompt]').should('have.text', 'Please select a recipe (or insert a new one if you have none!)')
    })
})
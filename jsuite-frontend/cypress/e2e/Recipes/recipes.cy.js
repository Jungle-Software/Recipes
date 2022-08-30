/// <reference types="cypress" />
import { hasOperationName } from '../../utils/graphql-test-utils'

describe('recipe page', () => {
    const recipeApiUrl = Cypress.env('apiUrl') + '/recipes';

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

    it('renders a selector button for each recipe', () => {
        cy.visit('/recipes')
        cy.get('[id=selector-button-1]').should('have.text', 'Cypress Mock Recipe')
        cy.get('[id=selector-button-2]').should('have.text', 'Cypress Mock Recipe 2')
    })

    it('renders recipe information if selector button pressed', () => {
        cy.visit('/recipes')
        cy.get('[id=selector-button-1]').click()
        cy.get('[id=recipe-view]')
          .invoke('text')
          .should('contain', "Cypress UNIVERSAL Recipe")
          .should('contain', "This is for Cypress e2e tests~")
          .should('contain', "4")
          .should('contain', "20")
          .should('contain', "40")
          .should('contain', "This will change when Guigui changes the schema")
          .should('contain', "Unclear")
          .should('contain', "None")
          .should('contain', "Absolutely none")
          .should('contain', "2022-06-09")
    })
})

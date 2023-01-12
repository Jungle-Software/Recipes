/// <reference types="cypress" />
import { hasOperationName } from '../../utils/graphql-test-utils'

describe('recipe page', () => {
    it('prompts the user to select a recipe', () => {
        cy.visit('/recipes')
        cy.get('[id=select-recipe-prompt]').should('have.text', 'Please select a recipe (or insert a new one if you have none!)')
    })

    it('renders a selector button for each recipe', () => {
        cy.visit('/recipes')
        cy.get('[id=selector-button-1]').should('have.text', 'The Best Brownies in the World')
    })

    it('renders recipe information if selector button pressed', () => {
        cy.visit('/recipes')
        cy.get('[id=selector-button-1]').click()
        cy.get('[id=recipe-view]')
          .invoke('text')
          .should('contain', "The Best Brownies in the World")
          .should('contain', "Description: Dense, fudgy brownies. Most people love them, those who don't are wrong.")
          .should('contain', "Categories:")
            .should('contain', "Dessert,")
          .should('contain', "Servings: 16")
          .should('contain', "Preparation time: 20 minutes")
          .should('contain', "Cooking time: 25 minutes")
          .should('contain', "Ingredients:")
            .should('contain', "0.2500 TEASPOON Salt")
            .should('contain', "0.5000 CUP Flour")
            .should('contain', "0.5000 TEASPOON Vanilla")
            .should('contain', "2.0000 UNIT Eggs Eggs")
            .should('contain', "1.0000 CUP Granulated Sugar")
            .should('contain', "0.5000 CUP Cocoa")
            .should('contain', "0.5000 CUP Butter Dairy")
          .should('contain', "Instructions:")
            .should('contain', "1. Prepare Mixture")
                .should('contain', "1.1. Melt butter in a large bowl.")
                .should('contain', "1.2. Mix cocoa, sugar, eggs, vanilla, flour, and salt with the melted butter")
            .should('contain', "2. Bake!")
                .should('contain', "2.1. Grease 8\" square pan.")
                .should('contain', "2.2. Spread brownie mixture into the pan.")
                .should('contain', "2.3. Bake at 350deg for 20-25 mins.")


            .should('contain', "Additional Notes: Do yourself a favor and double the recipe, because a single batch just simply isn't enough.")
          .should('contain', "Date last updated: 2023-01-12")
          .should('contain', "Date created: 2023-01-12")
    })
})

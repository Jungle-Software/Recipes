describe('recipes api testing', () => {
    const apiUrl = Cypress.env('apiUrl');

    // allRecipes query
    it('given well formed query, returns ok status', () => {
        cy.request({
            url: apiUrl + '/recipes',
            method: 'GET',
            body: {
                query: `
                query {
                    allRecipes {
                      id
                      title
                    }
                }`
            }
        }).as('allRecipesRequest');
        cy.get('@allRecipesRequest').then(recipes => {
            expect(recipes.status).to.eq(200);
        });
    });

    // recipeById query
    it('given well formed query, fetches recipe by id', () => {
        cy.request({
            url: apiUrl + '/recipes',
            method: 'GET',
            body: {
                query: `  
                query {
                    recipeById(id: 3) {
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
                }`
            }
        }).as('allRecipesRequest');
        cy.get('@allRecipesRequest').then(recipes => {
            expect(recipes.status).to.eq(200);
        });
    });

    // any bad query on the /recipes endpoint
    it('given badly formed query, returns bad request status', () => {
        cy.request({
            url: apiUrl + '/recipes',
            method: 'GET',
            failOnStatusCode: false,
            body: {
                query: `query { }`
            }
        }).as('allRecipesRequest');
        cy.get('@allRecipesRequest').then(recipes => {
            expect(recipes.status).to.eq(400);
        });
    });
 });
describe('recipe page', () => {
    it('should pass i stg', () => {
        cy.visit('/')
        cy.get('[id=shared-temp]').should('have.text', 'Bootstrap button :eyes:')
    })
})
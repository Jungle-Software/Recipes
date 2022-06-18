import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    specPattern: 'cypress/{e2e,api,temp}/**/*.cy.{js,jsx,ts,tsx}',
    baseUrl: 'http://localhost:3000',
    env: {
      apiUrl: 'http://localhost:8080/graphql',
  
    },
    video: false,
  },
});

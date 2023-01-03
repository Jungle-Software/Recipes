import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    specPattern: 'cypress/{e2e,}/**/*.cy.{js,jsx,ts,tsx}',
    baseUrl: 'http://127.0.0.1:3000',
    env: {
      apiUrl: 'http://127.0.0.1:8080/graphql',
  
    },
    video: false,
  },
});

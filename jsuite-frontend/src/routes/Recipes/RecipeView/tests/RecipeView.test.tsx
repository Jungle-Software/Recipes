import { render, cleanup } from "@testing-library/react";
import { MockedProvider } from "@apollo/client/testing";
import RecipeView, { RECIPE_BY_ID_QUERY } from "../RecipeView";

afterEach(cleanup);

const defaultRecipeMock = {
  request: {
    query: RECIPE_BY_ID_QUERY,
    variables: {
      id: 0,
    },
  },
  result: {
    data: {
      recipeById: null,
    },
  },
};

const recipeMock = {
  request: {
    query: RECIPE_BY_ID_QUERY,
    variables: {
      id: 1,
    },
  },
  result: {
    data: {
      recipeById: {
        id: 1,
        title: "Test Recipe 1",
        description: "testerino",
        portionSize: 0,
        prepTime: 0,
        cookTime: 0,
        ingredients: "",
        instructions: "",
        additionalNotes: "",
        nutritionalInfo: "",
        dateCreated: "",
      },
    },
  },
};

test("if no recipe is selected, then renders the 'Select a recipe' prompt", () => {
  // recipeID is 0 by default when no recipe is selected
  const { getByText } = render(
    <MockedProvider mocks={[defaultRecipeMock]} addTypename={false}>
      <RecipeView recipeId={0} />
    </MockedProvider>
  );

  expect(
    getByText("Please select a recipe (or insert a new one if you have none!)")
  ).toBeInTheDocument();
});

test("if a recipe is selected, then renders the recipe", async () => {
  const { findByText } = render(
    <MockedProvider mocks={[recipeMock]} addTypename={false}>
      <RecipeView recipeId={1} />
    </MockedProvider>
  );

  const recipeTitle = await findByText("testerino", { exact: false });
  expect(recipeTitle).toBeInTheDocument();
});

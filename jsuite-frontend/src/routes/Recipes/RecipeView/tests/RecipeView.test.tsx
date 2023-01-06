import { render, cleanup } from "@testing-library/react";
import { MockedProvider } from "@apollo/client/testing";
import RecipeView, { RECIPE_BY_ID_QUERY } from "../RecipeView";
import { BASE_ERROR_MESSAGE, SELECT_RECIPE_PROMPT } from "../../../../constants";

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
        title: "Test Recipe 1",
        description: "testerino",
        categories: [
            {
                name : "CategoryName1"
            }
        ],
        servings: 0,
        prepTime: 0,
        cookTime: 0,
        ingredients: [
            {
                ingredient: [
                  {
                    name: "IngredientName1",
                    allergens: [
                      {
                        type: "IngredientAllergenType1"
                      }
                    ],
                  }
                ],
                quantity: "0",
                unit: "MILLILITER",
            }
        ],
        instructions: [
          {
            subInstructions: [
              {
                text: "SubInstruction1"
              }
            ],
            text: "Instruction1"
          }
        ],
        additionalNotes: "",
        dateUpdated: "",
        dateCreated: "",
      },
    },
  },
};

const errorRecipeRequestMock = {
  request: {
    query: RECIPE_BY_ID_QUERY,
    variables: {},
  },
  error: new Error(),
};

// recipeID is 0 by default when no recipe is selected
it("renders loading message while fetching data", async () => {
  const { findByText } = render(
    <MockedProvider mocks={[defaultRecipeMock]} addTypename={false}>
      <RecipeView recipeId={1} />
    </MockedProvider>
  );

  const loadingMessage = await findByText("Loading", {exact: false});
  expect(loadingMessage).toBeInTheDocument();
});

it("renders dev error given a bad request (this shouldn't happen in production... in theory)", async () => {
  const { findByTestId } = render(
    <MockedProvider mocks={[errorRecipeRequestMock]} addTypename={false}>
      <RecipeView recipeId={1} />
    </MockedProvider>
  );

  const errorMessage = await findByTestId("error");
  expect(errorMessage).toBeInTheDocument();
});

it("if no recipe is selected, then renders the 'Select a recipe' prompt", async () => {
  const { findByText } = render(
    <MockedProvider mocks={[defaultRecipeMock]} addTypename={false}>
      <RecipeView recipeId={0} />
    </MockedProvider>
  );

  const recipePrompt = await findByText(SELECT_RECIPE_PROMPT)
  expect(recipePrompt).toBeInTheDocument();
});

it("if a recipe is selected, then renders the recipe", async () => {
  const { findByText } = render(
    <MockedProvider mocks={[recipeMock]} addTypename={false}>
      <RecipeView recipeId={1} />
    </MockedProvider>
  );

  const recipeTitle = await findByText("testerino", { exact: false });
  expect(recipeTitle).toBeInTheDocument();
});

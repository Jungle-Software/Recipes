import { render, cleanup } from "@testing-library/react";
import { MockedProvider } from "@apollo/client/testing";
import Recipes, { ALL_RECIPES_QUERY } from "../Recipes";

afterEach(cleanup);

const noRecipesMock = {
  request: {
    query: ALL_RECIPES_QUERY,
    variables: {},
  },
  result: {
    data: {
      allRecipes: [],
    },
  },
};

const recipesMock = {
  request: {
    query: ALL_RECIPES_QUERY,
    variables: {},
  },
  result: {
    data: {
      allRecipes: [
        { id: 1, title: "Test Recipe 1" },
        { id: 2, title: "Test Recipe 2" },
      ],
    },
  },
};

const errorRecipeRequestMock = {
  request: {
    query: ALL_RECIPES_QUERY,
    variables: {},
  },
  error: new Error(),
};

it("renders loading message while fetching data", async () => {
  const { findByText } = render(
    <MockedProvider mocks={[noRecipesMock]} addTypename={false}>
      <Recipes />
    </MockedProvider>
  );

  const loadingMessage = await findByText("Loading", {exact: false});
  expect(loadingMessage).toBeInTheDocument();
});

it("renders recipe page with no available recipes", async () => {
  const { findByText } = render(
    <MockedProvider mocks={[noRecipesMock]} addTypename={false}>
      <Recipes />
    </MockedProvider>
  );

  const recipePrompt = await findByText("Please select a recipe (or insert a new one if you have none!)");
  expect(recipePrompt).toBeInTheDocument();
});

it("renders recipe page with recipes", async () => {
  const { findByText } = render(
    <MockedProvider mocks={[recipesMock]} addTypename={false}>
      <Recipes />
    </MockedProvider>
  );

  const recipeTitle = await findByText("Recipes");
  expect(recipeTitle).toBeInTheDocument();
});

it("renders dev error given a bad request (this shouldn't happen in production... in theory)", async () => {
  const { findByText } = render(
    <MockedProvider mocks={[errorRecipeRequestMock]} addTypename={false}>
      <Recipes />
    </MockedProvider>
  );

  const devErrorMessage = await findByText("fuck", {exact: false});  // This *should* be the only place where this word will ever pop up in the project
  expect(devErrorMessage).toBeInTheDocument();
});

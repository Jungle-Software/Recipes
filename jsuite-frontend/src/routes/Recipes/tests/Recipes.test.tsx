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
        { id: "1", title: "Test Recipe 1" },
        { id: "2", title: "Test Recipe 2" },
      ],
    },
  },
};

it("renders loading message while fetching data", async () => {
  const { getByText } = render(
    <MockedProvider mocks={[noRecipesMock]} addTypename={false}>
      <Recipes />
    </MockedProvider>
  );

  expect(getByText("Loading", { exact: false })).toBeInTheDocument();
});

it("renders recipe page with no available recipes", async () => {
  const { findByText } = render(
    <MockedProvider mocks={[noRecipesMock]} addTypename={false}>
      <Recipes />
    </MockedProvider>
  );

  const title = await findByText("Recipes");
  expect(title).toBeInTheDocument();
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
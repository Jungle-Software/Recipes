import { render, fireEvent, waitFor } from "@testing-library/react";
import { MockedProvider } from "@apollo/client/testing";
import Recipes, { ALL_RECIPES_QUERY } from "../Recipes";
import { SELECT_RECIPE_PROMPT } from "../../../constants";
import { RECIPE_BY_ID_QUERY } from "../RecipeView/RecipeView";
import { DELETE_RECIPE_BY_ID_MUTATION } from "../RecipeSelector/SelectorButtonGroup/SelectorDeleteButton/SelectorDeleteButton";

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

const recipesDeletedMock = {
  request: {
    query: ALL_RECIPES_QUERY,
    variables: {},
  },
  result: {
    data: {
      allRecipes: [
        { id: 2, title: "Test Recipe 2" },
      ],
    },
  },
};

const deleteRecipeMock = {
  request: {
    query: DELETE_RECIPE_BY_ID_MUTATION,
    variables: {
      id: 1,
    },
  },
  result: {
    data: {
      deleteRecipe: null,
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

  const recipePrompt = await findByText(SELECT_RECIPE_PROMPT);
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

it("renders dev error given a bad request", async () => {
  const { findByTestId } = render(
    <MockedProvider mocks={[errorRecipeRequestMock]} addTypename={false}>
      <Recipes />
    </MockedProvider>
  );

  const errorMessage = await findByTestId("error");
  expect(errorMessage).toBeInTheDocument();
});

it("given click on recipe view button, displays the view", async () => {
  const { findByText, findByTestId } = render(
    <MockedProvider mocks={[recipeMock, recipesMock]}>
      <Recipes />
    </MockedProvider>
  );

  const selectRecipe1 = await findByText("Test Recipe 1");
  fireEvent.click(selectRecipe1)

  const recipeView = await findByTestId("recipe-view")

  expect(selectRecipe1).toBeInTheDocument()
  expect(recipeView).toBeInTheDocument()
});

it("when delete button is clicked, and is confirmed, calls handleDelete function", async () => {
  window.confirm = jest.fn(() => true)

  const { findByTestId, getByText } = render(
    <MockedProvider mocks={[recipesMock, deleteRecipeMock, recipesDeletedMock]}>
      <Recipes />
    </MockedProvider>
  );

  const deleteRecipe1 = await findByTestId("delete-button-1");
  fireEvent.click(deleteRecipe1)
  
  await waitFor(()=>expect(getByText("Deleted!")).toBeInTheDocument())
});

it("when delete button is clicked, and is not confirmed, don't call handleDelete function", async () => {
  window.confirm = jest.fn(() => false)

  const { findByTestId, getByText } = render(
    <MockedProvider mocks={[recipesMock, deleteRecipeMock, recipesDeletedMock]}>
      <Recipes />
    </MockedProvider>
  );

  const deleteRecipe1 = await findByTestId("delete-button-1");
  fireEvent.click(deleteRecipe1)
  
  await waitFor(()=>expect(deleteRecipe1).toBeInTheDocument())
});

it("given a selected recipe and delete that recipe, display recipe select prompt", async () => {
  window.confirm = jest.fn(() => true)

  const { findByTestId, getByText } = render(
    <MockedProvider mocks={[recipeMock, recipesMock, deleteRecipeMock, recipesDeletedMock]}>
      <Recipes />
    </MockedProvider>
  );

  const selectRecipe1 = await findByTestId("selector-button-1");
  fireEvent.click(selectRecipe1)
  
  const recipe1View = await findByTestId("recipe-view");
  expect(recipe1View).toBeInTheDocument()

  const deleteRecipe1 = await findByTestId("delete-button-1");
  fireEvent.click(deleteRecipe1)
  
  await waitFor(()=>expect(getByText("Deleted!")).toBeInTheDocument())
  const selectRecipePrompt = await getByText(SELECT_RECIPE_PROMPT)
  expect(selectRecipePrompt).toBeInTheDocument()
});
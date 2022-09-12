import { fireEvent, render, waitFor } from "@testing-library/react";
import { MockedProvider } from "@apollo/client/testing";
import RecipeSelector from "../RecipeSelector";
import { DELETE_RECIPE_BY_ID_MUTATION } from "../SelectorButtonGroup/SelectorDeleteButton/SelectorDeleteButton";

const recipeIds = [
  { id: 1, title: "Test Recipe 1" },
  { id: 2, title: "Test Recipe 2" },
];

const defaultRecipeMock = {
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

it("given recipes, renders a list of button groups (one for each recipe)", async () => {
  const { findByText } = render(
    <MockedProvider>
      <RecipeSelector
        recipeIds={recipeIds}
        onRecipeSelect={jest.fn()}
        onRecipeDelete={jest.fn()}
      />
    </MockedProvider>
  );

  const recipeTitle1 = await findByText("Test Recipe 1");
  const recipeTitle2 = await findByText("Test Recipe 2");

  expect(recipeTitle1).toBeInTheDocument();
  expect(recipeTitle2).toBeInTheDocument();
});

it("given click on recipe view button, calls onRecipeSelect", async () => {
  const doTheThing = jest.fn()

  const { findByText } = render(
    <MockedProvider>
      <RecipeSelector
        recipeIds={recipeIds}
        onRecipeSelect={doTheThing}
        onRecipeDelete={jest.fn()}
      />
    </MockedProvider>
  );

  const selectRecipe1 = await findByText("Test Recipe 1");
  fireEvent.click(selectRecipe1)

  expect(doTheThing).toBeCalledTimes(1)
});

it("when delete button is clicked, and is confirmed, calls onRecipeDelete", async () => {
  window.confirm = jest.fn(() => true)
  const doTheThing = jest.fn()

  const { findByTestId } = render(
    <MockedProvider mocks={[defaultRecipeMock]}>
      <RecipeSelector
        recipeIds={recipeIds}
        onRecipeSelect={jest.fn()}
        onRecipeDelete={doTheThing}
      />
    </MockedProvider>
  );

  const deleteRecipe1 = await findByTestId("delete-button-1");
  fireEvent.click(deleteRecipe1)

  await waitFor(() => expect(doTheThing).toBeCalledTimes(1))
});

it("when delete button is clicked, and is not confirmed, don't call onRecipeDelete", async () => {
  window.confirm = jest.fn(() => false)
  const doTheThing = jest.fn()

  const { findByTestId } = render(
    <MockedProvider mocks={[defaultRecipeMock]}>
      <RecipeSelector
        recipeIds={recipeIds}
        onRecipeSelect={jest.fn()}
        onRecipeDelete={doTheThing}
      />
    </MockedProvider>
  );

  const deleteRecipe1 = await findByTestId("delete-button-1");
  fireEvent.click(deleteRecipe1)

  await waitFor(() => expect(doTheThing).toBeCalledTimes(0))
});

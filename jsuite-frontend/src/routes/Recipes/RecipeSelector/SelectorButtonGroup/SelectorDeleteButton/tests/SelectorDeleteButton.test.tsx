import { MockedProvider } from "@apollo/client/testing";
import { fireEvent, render, waitFor } from "@testing-library/react";
import SelectorDeleteButton, { DELETE_RECIPE_BY_ID_MUTATION } from "../SelectorDeleteButton";

const recipeId = { id: 1, title: "Test Recipe 1" }

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

const errorRecipeRequestMock = {
    request: {
      query: DELETE_RECIPE_BY_ID_MUTATION,
      variables: {
        id: 1,
      },
    },
    error: new Error(),
  };
  
it("when delete button is clicked, and is confirmed, call handleClick", async () => {
  window.confirm = jest.fn(() => true)
  const doTheThing = jest.fn()

  const { findByTestId } = render(
      <MockedProvider mocks={[defaultRecipeMock]}>
      <SelectorDeleteButton
          recipe={recipeId}
          handleClick={doTheThing}
      />
      </MockedProvider>
  );

  const deleteButton = await findByTestId("delete-button-1");
  fireEvent.click(deleteButton);

  await waitFor(() => expect(doTheThing).toBeCalledTimes(1))
})

it("when delete button is clicked, and is not confirmed, don't call handleClick", async () => {
  window.confirm = jest.fn(() => false)
  const doTheThing = jest.fn()

  const { findByTestId } = render(
      <MockedProvider mocks={[defaultRecipeMock]}>
      <SelectorDeleteButton
          recipe={recipeId}
          handleClick={doTheThing}
      />
      </MockedProvider>
  );

  const deleteButton = await findByTestId("delete-button-1");
  fireEvent.click(deleteButton);

  await waitFor(() => expect(doTheThing).toBeCalledTimes(0))
})

it("when delete button is clicked, and is confirmed, renders dev error given a bad request (this shouldn't happen in production... in theory)", async () => {
  window.confirm = jest.fn(() => true)
  const doTheThing = jest.fn()

  const { findByTestId } = render(
    <MockedProvider mocks={[errorRecipeRequestMock]}>
      <SelectorDeleteButton
        recipe={recipeId}
        handleClick={doTheThing}
    />
    </MockedProvider>
  );

  const deleteButton = await findByTestId("delete-button-1");
  fireEvent.click(deleteButton)

  const errorMessage = await findByTestId("error")
  expect(errorMessage).toBeInTheDocument()
});

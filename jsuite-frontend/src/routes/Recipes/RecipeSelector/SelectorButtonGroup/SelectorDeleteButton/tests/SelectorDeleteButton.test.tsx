import { MockedProvider } from "@apollo/client/testing";
import { act, findByText, fireEvent, getByTestId, render, waitFor } from "@testing-library/react";
import { wait } from "@testing-library/user-event/dist/utils";
import { BASE_ERROR_MESSAGE } from "../../../../../../constants";
import SelectorDeleteButton, { DELETE_RECIPE_BY_ID_QUERY } from "../SelectorDeleteButton";

const recipeId = { id: 1, title: "Test Recipe 1" }

const defaultRecipeMock = {
    request: {
      query: DELETE_RECIPE_BY_ID_QUERY,
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
      query: DELETE_RECIPE_BY_ID_QUERY,
      variables: {
        id: 1,
      },
    },
    error: new Error(),
  };
  
it("when delete button is clicked, call handleClick", async () => {
const doTheThing = jest.fn()

const { findByTestId } = render(
    <MockedProvider mocks={[defaultRecipeMock]}>
    <SelectorDeleteButton
        id={recipeId.id}
        handleClick={doTheThing}
    />
    </MockedProvider>
);

const deleteButton = await findByTestId("delete-button-1");
fireEvent.click(deleteButton);

await waitFor(() => expect(doTheThing).toBeCalledTimes(1))
})

it("when delete button is clicked, renders dev error given a bad request (this shouldn't happen in production... in theory)", async () => {
  const doTheThing = jest.fn()

  const { findByTestId, debug } = render(
    <MockedProvider mocks={[errorRecipeRequestMock]}>
      <SelectorDeleteButton
        id={recipeId.id}
        handleClick={doTheThing}
    />
    </MockedProvider>
  );

  const deleteButton = await findByTestId("delete-button-1");
  fireEvent.click(deleteButton)

  const errorMessage = await findByTestId("error")
  expect(errorMessage).toBeInTheDocument()
});

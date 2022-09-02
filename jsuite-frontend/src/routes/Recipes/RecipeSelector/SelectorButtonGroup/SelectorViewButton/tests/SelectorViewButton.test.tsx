import { fireEvent, render } from "@testing-library/react";
import { MockedProvider } from "@apollo/client/testing";
import SelectorViewButton from "../SelectorViewButton";

const recipeId = { id: 1, title: "Test Recipe 1" }

it("when view button is clicked, call handleClick", async () => {
    const doTheThing = jest.fn()
  
    const { findByText } = render(
      <MockedProvider>
        <SelectorViewButton
          recipe={recipeId}
          handleClick={doTheThing}
        />
      </MockedProvider>
    );
  
    const recipeButton1 = await findByText("Test Recipe 1");
    fireEvent.click(recipeButton1);
  
    expect(doTheThing).toBeCalledTimes(1);
  })
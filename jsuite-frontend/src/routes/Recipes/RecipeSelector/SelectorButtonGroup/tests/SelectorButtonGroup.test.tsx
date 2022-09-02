import { render } from "@testing-library/react";
import { MockedProvider } from "@apollo/client/testing";
import SelectorButtonGroup from "../SelectorButtonGroup";

const recipe = {id: 1, title: "Test Recipe 1"}
it("given a recipe, renders a button group for read update and delete operations", async () => {
  const { findByText, findByTestId } = render(
    <MockedProvider>
      <SelectorButtonGroup
        recipe={recipe}
        onRecipeSelect={jest.fn()}
        onRecipeDelete={jest.fn()}
      />
    </MockedProvider>
  );

  const recipeTitle1 = await findByText("Test Recipe 1");
  const recipeTitle2 = await findByTestId("delete-button-1");

  expect(recipeTitle1).toBeInTheDocument();
  expect(recipeTitle2).toBeInTheDocument();
});
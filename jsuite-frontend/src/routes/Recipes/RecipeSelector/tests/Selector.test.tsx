import { render } from "@testing-library/react";
import Selector from "../Selector";

const recipeIds = [
  { id: 1, title: "Test Recipe 1" },
  { id: 2, title: "Test Recipe 2" },
];

it("given recipes, renders a list of buttons (one for each recipe)", async () => {
  const { findByText } = render(
    <Selector
      recipeIds={recipeIds}
      onRecipeChange={jest.fn()}
    />
  );

  const recipeTitle1 = await findByText("Test Recipe 1");
  const recipeTitle2 = await findByText("Test Recipe 2");

  expect(recipeTitle1).toBeInTheDocument();
  expect(recipeTitle2).toBeInTheDocument();
});

it("when button is clicked, call handleClick", async () => {
  const { findByText } = render(
    <Selector
      recipeIds={recipeIds}
      onRecipeChange={jest.fn()}
    />
  );
})

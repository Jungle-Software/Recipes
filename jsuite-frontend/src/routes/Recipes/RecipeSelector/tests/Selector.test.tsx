import { render } from "@testing-library/react";
import Selector from "../Selector";

const recipeIDs = [
  { id: "1", title: "Test Recipe 1" },
  { id: "2", title: "Test Recipe 2" },
];

it("given recipes, renders a list of buttons (one for each recipe)", async () => {
  const { findByText } = render(<Selector recipeIDs={recipeIDs} />);

  const recipeTitle1 = await findByText("Test Recipe 1");
  const recipeTitle2 = await findByText("Test Recipe 2");

  expect(recipeTitle1).toBeInTheDocument();
  expect(recipeTitle2).toBeInTheDocument();
});

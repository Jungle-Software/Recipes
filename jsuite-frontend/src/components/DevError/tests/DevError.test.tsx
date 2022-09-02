import { findByTestId, render } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { BASE_ERROR_MESSAGE } from "../../../constants";
import DevError from "../DevError";

it("renders dev error component", async () => {
  const { findByTestId } = render(
    <MemoryRouter>
      <DevError message=""/>
    </MemoryRouter>
  );
  const errorMessage = await findByTestId("error");
  expect(errorMessage).toBeInTheDocument();
});

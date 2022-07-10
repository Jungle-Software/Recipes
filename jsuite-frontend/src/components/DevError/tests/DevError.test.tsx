import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import DevError from "../DevError";

it("renders dev error component", async () => {
  const { findByText } = render(
    <MemoryRouter>
      <DevError />
    </MemoryRouter>
  );
  const titleElement = await findByText("fuck", { exact: false });
  expect(titleElement).toBeInTheDocument();
});

import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import DevError from "../DevError";

test("renders dev error component", () => {
  render(
    <MemoryRouter>
      <DevError />
    </MemoryRouter>
  );
  const titleElement = screen.getByText(/fuck/i);
  expect(titleElement).toBeInTheDocument();
});

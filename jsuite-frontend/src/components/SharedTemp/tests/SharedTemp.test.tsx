import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import SharedTemp from '../SharedTemp';

it('renders shared temp component', async () => {
  const { findByText } = render(
    <MemoryRouter>
      <SharedTemp />
    </MemoryRouter>
  );
  const titleElement = await findByText("Shared", { exact: false });
  expect(titleElement).toBeInTheDocument();
});

import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import SharedTemp from '../SharedTemp';

test('renders shared temp component', () => {
  render(
    <MemoryRouter>
        <SharedTemp />
    </MemoryRouter>
  );
  const titleElement = screen.getByText(/Shared/i);
  expect(titleElement).toBeInTheDocument();
});

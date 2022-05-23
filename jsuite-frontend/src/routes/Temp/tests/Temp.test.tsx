import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Temp from '../Temp';

test('renders temp landing page link', () => {
  render(
    <MemoryRouter>
        <Temp />
    </MemoryRouter>
  );
  const titleElement = screen.getByText(/JSuite/i);
  expect(titleElement).toBeInTheDocument();
});

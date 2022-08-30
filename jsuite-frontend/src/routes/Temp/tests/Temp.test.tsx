import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Temp from '../Temp';

it('renders temp landing page link', async () => {
  const { findByText } = render(
    <MemoryRouter>
      <Temp />
    </MemoryRouter>
  );
  const titleElement = await findByText("Welcome to JSuite!", { exact: true });
  expect(titleElement).toBeInTheDocument();
});

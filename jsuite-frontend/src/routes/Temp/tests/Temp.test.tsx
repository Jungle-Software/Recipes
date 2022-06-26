import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Temp from '../Temp';

it('renders temp landing page link', async () => {
  const { findByText } = render(
    <MemoryRouter>
      <Temp />
    </MemoryRouter>
  );
  const titleElement = await findByText("JSuite", { exact: false });
  expect(titleElement).toBeInTheDocument();
});

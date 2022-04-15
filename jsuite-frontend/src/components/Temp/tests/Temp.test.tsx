import { render, screen } from '@testing-library/react';
import Temp from '../Temp';

test('renders temp landing page link', () => {
  render(<Temp />);
  const titleElement = screen.getByText(/JSuite/i);
  expect(titleElement).toBeInTheDocument();
});

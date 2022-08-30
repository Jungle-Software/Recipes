import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import NavBar from '../NavBar';

it('render navBar component', async () => {
    const { findByText } = render(
        <MemoryRouter>
            <NavBar />
        </MemoryRouter>
    );
    const navbarElement = await findByText("Jrecipe", { exact: false});
    expect(navbarElement).toBeInTheDocument();
});
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import NavBar from '../NavBar';

test('render navBar component', () => {
    render(
        <MemoryRouter>
            <NavBar />
        </MemoryRouter>
    );

});
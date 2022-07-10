//import { } from './NavBar.styles'
import {Link} from 'react-router-dom';
import Navbar from 'react-bootstrap/Navbar'
import Container from 'react-bootstrap/Container'
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'



const NavBar = () => {
    return (
        <Navbar bg="light" expand="lg">
            <Container>
                <Navbar.Brand href="/">Jsuite</Navbar.Brand>
                <Navbar.Toggle aria-controls="jsuite-navbar" />
                <Navbar.Collapse id="jsuite-navbar">
                    <Nav className="me-auto">
                        <Nav.Link href="recipes">Jrecipe</Nav.Link>
                        <Nav.Link href="#link">About</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );

}

export default NavBar;
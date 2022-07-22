import { HashRouter, Outlet, Route, Routes, Navigate } from "react-router-dom";
import { Navbar, Container, Nav, NavDropdown } from "react-bootstrap";
import LoginPage from "./features/auth/LoginPage";
import DashboardPage from "./features/dashboard/DashboardPage";
import MapPage from "./features/map/MapPage";
import { PersonFill } from "react-bootstrap-icons";

export default function Router() {
    return <HashRouter>
        <Routes>
            <Route path="/" element={<WithNavbar />}>
                <Route path="/" element={<Navigate to="/dashboard" replace />} />
                <Route path="dashboard" element={<DashboardPage />}>
                    <Route path=":vesselId" element={<DashboardPage />} />
                </Route>
                <Route path="/map" element={<MapPage />} />
            </Route>
            <Route path="/login" element={<LoginPage />} />
        </Routes>
    </HashRouter>
}

function WithNavbar() {
    return <div className="d-flex flex-column min-vh-100">
        <Navbar collapseOnSelect expand="sm" bg="dark" variant="dark" className="py-sm-3">
            <Container fluid className="px-sm-5">
                <Navbar.Brand href="#/">MarineAnalyitcs</Navbar.Brand>
                <Navbar.Toggle aria-controls="navbar" />
                <Navbar.Collapse id="navbar">
                    <Nav className="me-auto">
                        <Nav.Link href="#/dashboard">Суда</Nav.Link>
                        <Nav.Link href="#/map">Карта</Nav.Link>
                        <Nav.Link href="#/about">О нас</Nav.Link>
                    </Nav>
                    <Nav>
                        <NavDropdown title={<PersonFill size={24} />} id="collasible-nav-dropdown" align={'end'}>
                            <NavDropdown.Header>admin@mail.com</NavDropdown.Header>
                            <NavDropdown.Item href="#">Личный кабинет</NavDropdown.Item>
                            <NavDropdown.Item href="#">Настройки</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item href="#">Выйти из аккаунта</NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>

        <Outlet />

        <footer className="py-2 mt-auto bg-light">
            <p className="text-center text-muted my-1">© 2022 MarineAnalytics</p>
        </footer>
    </div>
}
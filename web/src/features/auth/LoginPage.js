import { Form, Button, FloatingLabel, Card } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
    const navigate = useNavigate();

    return <div className='min-vh-100 d-flex' style={{
        backgroundImage: 'linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("static/login-bg.jpg")',
    }}>
        <div class="form-signin w-100 m-auto p-4" style={{
            maxWidth: '440px',
        }}>
            <Card className='p-5 shadow'>
                <Form>
                    <h1 class="h3 mb-4 text-center" style={{ fontWeight: '400' }}>Вход в аккаунт</h1>
                    <Form.Group className="mb-3" controlId="email">
                        <FloatingLabel controlId="email" label="Эл. почта">
                            <Form.Control type="email" placeholder="Эл. почта" style={{
                                borderBottomLeftRadius: '0',
                                borderBottomRightRadius: '0',
                                marginBottom: '-1px'
                            }} />
                        </FloatingLabel>
                        <FloatingLabel controlId="password" label="Пароль"  >
                            <Form.Control type="password" placeholder="Пароль" style={{
                                borderTopLeftRadius: '0',
                                borderTopRightRadius: '0',
                            }} />
                        </FloatingLabel>
                    </Form.Group>

                    <Button variant="primary" type="submit" onClick={() => { navigate("/map") }} className="w-100 py-2">
                        Войти
                    </Button>

                    <div className="text-center mt-3">
                        <a href="?" class="mt-3 mb-0 text-muted">Демо</a>
                        <span class="mt-3 mb-0 text-muted mx-2">&#8226;</span>
                        <a href="?" class="mt-3 mb-0 text-muted">О нас</a>
                    </div>
                </Form>
            </Card>
        </div>
    </div>
}
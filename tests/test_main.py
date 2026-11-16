from app.main import app, sumar


def cliente():
    app.config["TESTING"] = True
    return app.test_client()


def test_sumar():
    assert sumar(2, 3) == 5


def test_health():
    respuesta = cliente().get("/health")
    assert respuesta.status_code == 200
    assert respuesta.get_json() == {"status": "ok"}


def test_inicio():
    respuesta = cliente().get("/")
    assert respuesta.status_code == 200
    assert b"Hola desde AWS" in respuesta.data


def test_ruta_sumar():
    respuesta = cliente().get("/sumar/4/6")
    assert respuesta.get_json() == {"resultado": 10}

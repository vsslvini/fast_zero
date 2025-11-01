from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_ola_deve_retornar_html_com_ola_mundo():
    client = TestClient(app)

    response = client.get('/ola')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo!</h1>' in response.text

BASE = '/user'


def test_ping(client):
    response = client.get(f'{BASE}/ping')
    assert response.status_code == 200
    assert response.json.get('mensaje') == 'pong'


def test_login_incorrect(client):
    response = client.post(f'{BASE}/login', data={
        'correo': 'prueba@prueba.com',
        'contrasena': '000'
    })
    #print("response.json:", response.json)
    assert response.status_code == 400
    #assert 'el usuario no esta activo' == response.json.get('mensaje')


def test_verificar_incorrect(client):
    response = client.post(f'{BASE}/verifyemail', data={'token':'123'})
    assert response.status_code == 400
    assert 'error' in response.json
    #assert 'Error en token invalido' == response.json.get('mensaje')



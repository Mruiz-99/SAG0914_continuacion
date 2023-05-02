BASE = '/inventario'


def test_ping(client):
    response = client.get(f'{BASE}/ping')
    assert response.status_code == 200
    assert response.json.get('mensaje') == 'pong'


def test_getcategorias_correct(client):
    response = client.get(f'{BASE}/getcategorias', data={
    })
    #print("response.json:", response.json)
    assert response.status_code == 200
    #assert 'el usuario no esta activo' == response.json.get('mensaje')


def test_getproductos_correct(client):
    response = client.get(f'{BASE}/getproductos', data={})
    assert response.status_code == 200
    #assert 'error' in response.json
    #assert 'Error en token invalido' == response.json.get('mensaje')




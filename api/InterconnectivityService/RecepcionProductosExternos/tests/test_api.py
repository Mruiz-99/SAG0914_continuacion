
def test_ping(client):
    response = client.get(f'/ping')
    assert response.status_code == 200
    assert response.json.get('mensaje') == 'pong'


def test_error_recepcion_productos(client):
    response = client.put(f'/inventario/recepcion')
    assert response.status_code == 400

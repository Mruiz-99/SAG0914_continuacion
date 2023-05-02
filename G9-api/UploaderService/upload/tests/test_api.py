from pathlib import Path

BASE = '/bucket'
resources = Path(__file__).parent / 'resources'


def test_ping(client):
    response = client.get(f'{BASE}/ping')
    assert response.status_code == 200
    assert response.json.get('mensaje') == 'pong'


def test_upload_file_incorrect(client):
    response = client.post(f'{BASE}/upload', data={

    })
    assert response.status_code == 400
    assert 'error' in response.json
    assert 'Archivo es requerido' == response.json.get('mensaje')


def test_upload_file_correct(client):
    response = client.post(f'{BASE}/upload', data={
        'archivo': (resources / 'imagen.png').open('rb')
    })
    assert response.status_code == 200
    assert 'error' not in response.json
    assert 'data' in response.json
    assert 'Objeto Almacenado' == response.json.get('mensaje')


def test_upload_file_size(client):
    response = client.post(f'{BASE}/upload', data={
        'archivo': (resources / 'imagen2.jpg').open('rb')
    })
    assert response.status_code == 413
    assert 'error' in response.json
    assert 'data' not in response.json
    assert 'Error al almacenar el objeto' == response.json.get('mensaje')


def test_upload_file_not_image(client):
    response = client.post(f'{BASE}/upload', data={
        'archivo': (resources / 'file.txt').open('rb')
    })
    assert response.status_code == 400
    assert 'error' in response.json
    assert 'data' not in response.json

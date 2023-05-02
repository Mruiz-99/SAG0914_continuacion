BASE = '/notification'


def test_ping(client):
    response = client.get(f'{BASE}/ping')
    assert response.status_code == 200
    assert response.json.get('mensaje') == 'pong'


def teste_send_email_correct(client):
    response = client.post(f'{BASE}/sendEmail', data={
        'para': 'afml183@gmail.com',
        'asunto': 'TEST',
        'mensaje': 'cuerpo del mensaje'
    })
    assert response.status_code == 200
    assert 'Correo enviado' == response.json.get('mensaje')


def teste_send_email_incorrect(client):
    response = client.post(f'{BASE}/sendEmail', data={})
    assert response.status_code == 400
    assert 'error' in response.json
    assert 'Error con los campos.' == response.json.get('mensaje')




def test_agregar_productos_carrito(client):
    response = client.post('/rrhh/agendarEntrevista', headers={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZFVzdWFyaW8iOiIyOTk0OTAyNDYwMTA5IiwidGlwb1VzdWFyaW8iOjEsImV4cCI6MTY4NDgxMDY1OH0.3TeWxFKkIxPKO0mo4A4wsvvVrsFF0QqOdr919q7XbYY'
    }, data={
        'cui':2994902460101,
        'nombres':'Mynor Ricardo',
        'apellidos':'Perez',
        'correo':'mynorreneruizguerra@gmail.com',
        'fechaCita':'2023-05-1 12:00:00'
    })
    assert response.status_code == 200
    print(type(response.json.get('data')))
    assert isinstance(response.json.get('mensaje'), str)

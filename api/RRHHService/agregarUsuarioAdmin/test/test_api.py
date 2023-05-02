
def test_agregar_usuario_administrativo(client):
    response = client.post('/rrhh/agregarUsuario', headers={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZFVzdWFyaW8iOiIyOTk0OTAyNDYwMTAxIiwidGlwb1VzdWFyaW8iOjEsImV4cCI6MTY4NDgxMDY1OH0.ArEk4AKlMGu1-HO0E6IFR4pK4F4I3ssPmpmPsl8KPBQ'
    }, data={
        'cui':2994902460101,
        'correo':'l@gmail.com',
        'apellidos':'Ruiz',
        'nombres':'Mynor',
        'password':'1234',
        'confirmarPassword':'1234',
        'areaAsignada':'Contabilidad',
        'fechaNacimiento':'1999/08/05',
        'sueldo':5000.00
    })
    assert response.status_code == 200
    print(type(response.json.get('data')))
    assert isinstance(response.json.get('mensaje'), str)

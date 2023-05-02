
def test_dar_baja_usuarios_administrativos(client):
    response = client.put('/rrhh/eliminarUsuarioAdmin', headers={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZFVzdWFyaW8iOiIyOTk0OTAyNDYwMTAxIiwidGlwb1VzdWFyaW8iOjEsImV4cCI6MTY4NDgxMDY1OH0.ArEk4AKlMGu1-HO0E6IFR4pK4F4I3ssPmpmPsl8KPBQ'
    }, data={
        'cui':2994902460117
    })
    assert response.status_code == 200
    print(type(response.json.get('data')))
    assert isinstance(response.json.get('mensaje'), str)

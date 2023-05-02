
def test_agregar_productos_carrito(client):
    response = client.post('/buy/addShoppingCart', headers={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZFVzdWFyaW8iOiIyOTk0OTAyNDYwMTAxIiwidGlwb1VzdWFyaW8iOiJFIiwiZXhwIjoxNjg0ODEwNjU4fQ.jvwqUkTR47ix6OVhkLpdPy-O4N86ucDWA5cdlY3z7uQ'
    }, data={
        'id_producto':1,
        'cantidad':2
    })
    assert response.status_code == 200
    print(type(response.json.get('data')))
    assert isinstance(response.json.get('mensaje'), str)

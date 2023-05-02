
def test_cancelarCompra(client):
    response = client.delete('/buy/emptyProductCart', headers={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZFVzdWFyaW8iOiIyOTk0OTAyNDYwMTAxIiwidGlwb1VzdWFyaW8iOiJFIiwiZXhwIjoxNjg0ODEwNjU4fQ.jvwqUkTR47ix6OVhkLpdPy-O4N86ucDWA5cdlY3z7uQ'
    })
    assert response.status_code == 200
    assert isinstance(response.json.get('mensaje'), str)

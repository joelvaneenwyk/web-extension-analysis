import core.__main__ as main


def test_version(client):
    response = client.get('/version/')

    # Check the response status code
    assert response.status_code == 200

    # Check the response JSON content
    data = response.data
    assert data == b"1.0.5"

from app import app

app.testing = True
client = app.test_client()


def test_index_page():
    response = client.get()
    assert response.status_code == 200

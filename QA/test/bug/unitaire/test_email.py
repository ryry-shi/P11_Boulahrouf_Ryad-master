from fichier_client import client
import server

def test_showshumarry_data_dont_found(client):
    response = client.post("/showSummary", data={"email": True})
    assert response.status_code == 200


def test_showshumarry_data_dont_found(client):
    response = client.post("/showSummary", data={"email": False})
    assert response.status_code == 200

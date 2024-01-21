from fichier_client import client
import server

def test_showshumarry(client):
    response = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert response.status_code == 200
    assert "john@simplylift.co" in response.get_data(as_text=True)

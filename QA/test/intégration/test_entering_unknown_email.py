from fichier_client import client
import server

def test_showshumarry_data_dont_found(client):
    response = client.post("/showSummary", data={"email": "unknow@email.fr"})
    assert response.status_code == 200
    assert "Désolé, cet e-mail n&#39;a pas été trouvé" in response.get_data(
        as_text=True
    )

from fichier_client import client
import server

clubs = server.loadClubs()
competitions = server.loadCompetitions()
    
def test_book_already_passe(client):
    club = [c for c in clubs if c["name"]][0]
    competition = [c for c in competitions if c["name"]][0]
    if club and competition:
        response = client.get(f"/book/Fall Classic/Simply Lift")
        assert response.status_code == 200
    assert "vous ne pouvez pas réservez une place pour un spectacle déja produit" in response.get_data(
        as_text=True
    )

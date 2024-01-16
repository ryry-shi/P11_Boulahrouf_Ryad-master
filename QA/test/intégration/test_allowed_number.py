from fichier_client import client
import server

clubs = server.loadClubs()
competitions = server.loadCompetitions()
    
def test_points_more_not_than_allowed(client, methods=["POST"]):
    club = [c for c in clubs if c["name"]][1]
    competition = [c for c in competitions if c["name"]][0]
    places = 5
    response = client.post(
        "/purchasePlaces",
        data={
            "places": places,
            "club": club["name"],
            "competition": competition["name"],
        },
    )
    
    assert response.status_code == 200
    assert "pas assez de points pour réservez de ticket" in response.get_data(
        as_text=True
    )

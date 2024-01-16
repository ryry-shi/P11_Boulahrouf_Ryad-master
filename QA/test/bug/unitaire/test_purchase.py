from fichier_client import client
import server

clubs = server.loadClubs()
competitions = server.loadCompetitions()
    
def test_purchase_more_than_valid_12_place(client, methods=["POST"]):
    places = 13
    response = client.post(
        "/purchasePlaces",
        data={
            "places": places,
            "club": "Simply Lift",
            "competition": "League Classic",
        },
    )
    assert response.status_code == 200
    assert (
        f"Vous ne pouvez pas réservez plus de 12 place"
        in response.get_data(as_text=True)
    )


    
def test_purchase_more_than_valid_12_place(client, methods=["POST"]):
    places = 12
    response = client.post(
        "/purchasePlaces",
        data={
            "places": places,
            "club": "Simply Lift",
            "competition": "League Classic",
        },
    )
    
    (response.get_data(as_text=True))
    assert response.status_code == 200
    assert (
        f"Points available: 1"
        in response.get_data(as_text=True)
    )
from fichier_client import client
import server

clubs = server.loadClubs()
competitions = server.loadCompetitions()
    
def test_purchase_valid_12_place(client, methods=["POST"]):
    club = [c for c in clubs if c["name"]][0]
    competition = [c for c in competitions if c["name"]][0]
    places = 13
    response = client.post(
        "/purchasePlaces",
        data={
            "places": places,
            "club": club["name"],
            "competition": competition["name"],
        },
    )
    assert response.status_code == 200
    assert (
        f"Points available: 1"
        in response.get_data(as_text=True)
    )


    
def test_purchase_valid_not_allowed_12_place(client, mocker, monkeypatch, methods=["POST"]):
    mock_load_club = mocker.patch(
        "server.clubs",
        [
            {"name": "a", "email": "utilisateur1.co", "points": "99"},
            {"name": "b", "email": "utilisateur2.com", "points": "15"},
            {"name": "c", "email": "utilisateur3co.uk", "points": "13"},
        ],
    )
    print(mock_load_club)
    monkeypatch.setattr("server.clubs", mock_load_club)
    mock_load_competition = mocker.patch(
        "server.competitions",
        [
            {"name": "chocolat", "date": "9999-12-12 12:12:12", "numberOfPlaces": "99"},
            {"name": "Vanille", "date": "1111-11-11 11:11:11", "numberOfPlaces": "11"},
        ],
    )
    monkeypatch.setattr("server.competitions", mock_load_competition)
    club = [c for c in mock_load_club if c["name"]][0]
    competition = [c for c in mock_load_competition if c["name"]][0]
    print(competition)
    places = 13
    if club:
        response = client.post(
            "/purchasePlaces",
            data={
                "places": places,
                "club": club["name"],
                "competition": competition["name"],
            },
        )
        assert response.status_code == 200
    assert (
        "Vous ne pouvez pas réservez plus de 12 place"
        in response.get_data(as_text=True)
    )

from fichier_client import client
import server

clubs = server.loadClubs()
competitions = server.loadCompetitions()


def test_reflected_points(client, methods=["POST"]):
    club = [c for c in clubs if c["name"]][0]
    competition = [c for c in competitions if c["name"]][0]
    if club and competition:
        response = client.post("/showSummary", data={"email": "john@simplylift.co"})
        assert response.status_code == 200
        assert "Points available: 4"
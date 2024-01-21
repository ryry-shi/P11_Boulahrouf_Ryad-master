from fichier_client import client
import server

clubs = server.loadClubs()
competitions = server.loadCompetitions()


def test_reflected_points(client, methods=["POST"]):
    club = [c for c in clubs if c["name"]][0]
    competition = [c for c in competitions if c["name"]][0]
    competition["numberOfPlaces"] = 5
    club["points"] = 6
    places = 6
    if competition["numberOfPlaces"] - club["points"] < places:
        True
        
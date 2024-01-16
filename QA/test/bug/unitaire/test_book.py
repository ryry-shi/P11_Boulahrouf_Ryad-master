from fichier_client import client
from flask import Flask, app
import datetime
import server
competitions = server.loadCompetitions()

def test_book_date_already_passed(client):
    response = client.get(f"/book/Fall Classic/Simply Lift")
    assert (f"un spectacle déja produit"in response.get_data(as_text=True))
    assert response.status_code == 200
    
def test_book_already_passe(client):
    response = client.get(f"/book/League Classic/Simply Lift")
    assert "League Classic" in response.get_data(as_text=True)
    assert response.status_code == 200


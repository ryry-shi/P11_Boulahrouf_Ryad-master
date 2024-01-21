from fichier_client import client
from flask import Flask
from typing import List

app = Flask(__name__)


@app.route("/")
def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


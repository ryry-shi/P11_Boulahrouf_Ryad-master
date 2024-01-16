from fichier_client import client

def test_index(client):
    response = client.get("/")
    assert "Please enter your secretary email to continue:" in response.get_data(
        as_text=True
    )
    

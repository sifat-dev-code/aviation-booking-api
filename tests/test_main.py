from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_api_docs_loads():
    response = client.get("/docs")
    assert response.status_code == 200

def test_get_all_flights():
    response = client.get("/flights/") 
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["data"], list)
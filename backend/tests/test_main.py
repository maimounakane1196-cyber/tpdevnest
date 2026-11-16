from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    # On appelle /health et on vérifie la réponse
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
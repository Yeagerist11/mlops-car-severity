
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_predict_endpoint():
    response = client.post(
        "/predict",
        json={
            "impact_speed": 70,
            "damage_score": 7,
            "airbag_deployed": 1,
        },
    )

    assert response.status_code == 200
    assert response.json()["predicted_severity"] in [
        "Moderate",
        "Severe",
    ]


def test_invalid_damage_score():
    response = client.post(
        "/predict",
        json={
            "impact_speed": 70,
            "damage_score": 15,
            "airbag_deployed": 1,
        },
    )

    assert response.status_code == 422

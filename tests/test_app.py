from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "remove-me@example.com"
    activities[activity_name]["participants"].append(email)

    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email},
    )

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]


def test_unregister_unknown_participant_returns_bad_request():
    activity_name = "Chess Club"
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": "missing@example.com"},
    )

    assert response.status_code == 400

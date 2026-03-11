from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange: No setup needed
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Arrange
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    # Act
    signup_response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert signup_response.status_code == 200
    assert signup_response.json()["message"] == f"Signed up {email} for {activity}"

    # Act
    unregister_response = client.post(f"/activities/{activity}/unregister?email={email}")
    # Assert
    assert unregister_response.status_code == 200
    assert unregister_response.json()["message"] == f"Unregistered {email} from {activity}"

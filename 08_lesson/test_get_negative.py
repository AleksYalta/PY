import requests
import uuid


def test_get_project_not_found(base_url, headers):
    non_existent_id = str(uuid.uuid4())

    response = requests.get(f"{base_url}/api-v2/projects/{non_existent_id}",
                            headers=headers)

    assert response.status_code == 404
    data = response.json()
    assert data["statusCode"] == 404
    assert data["message"] == "Проект не найден"
    assert data["error"] == "Not Found"

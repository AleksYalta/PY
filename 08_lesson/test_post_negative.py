import requests


def test_create_project_negative_empty_title(base_url, headers):
    payload = {
        "title": "",
        "users": {
            "10e6c06d-a00b-4e3a-8fee-d57417921ffa": "worker"
        }
    }

    response = requests.post(f"{base_url}/api-v2/projects",
                             headers=headers, json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "title should not be empty" in data.get("message", [])
    assert data["error"] == "Bad Request"

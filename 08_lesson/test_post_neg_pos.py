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


def test_create_project_positive(base_url, headers):
    payload = {
        "title": "ГосУслуги",
        "users": {
            "10e6c06d-a00b-4e3a-8fee-d57417921ffa": "worker"
        }
    }

    response = requests.post(f"{base_url}/api-v2/projects",
                             headers=headers, json=payload)

    print("Response status code:", response.status_code)
    print("Response content:", response.text)

    assert response.status_code == 201

    data = response.json()
    print("Response JSON:", data)

    assert "id" in data, "'id' field is missing in the response"
    assert isinstance(data["id"], str), "'id' should be a string"

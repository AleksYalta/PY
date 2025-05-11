import requests
from utils import generate_unique_project_name


def test_update_project_mark_deleted(base_url, headers):
    create_resp = requests.post(f"{base_url}/api-v2/projects",
                                headers=headers, json={
        "title": generate_unique_project_name(),
        "users": {
            "10e6c06d-a00b-4e3a-8fee-d57417921ffa": "worker"
        }
    })
    project_id = create_resp.json().get("id")

    print("Created project ID:", project_id)

    update_resp = requests.put(f"{base_url}/api-v2/projects/{project_id}",
                               headers=headers, json={
        "title": "ГосУслуги",
        "deleted": True,
        "users": {
            "10e6c06d-a00b-4e3a-8fee-d57417921ffa": "worker"
        }
    })

    print("Update Response status code:", update_resp.status_code)
    print("Update Response content:", update_resp.text)

    assert update_resp.status_code == 200

    data = update_resp.json()
    print("Update Response JSON:", data)

    assert "id" in data, "'id' field is missing in the response"
    assert isinstance(data["id"], str), "'id' should be a string"

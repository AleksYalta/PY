import requests
from utils import generate_unique_project_name


def test_update_project_empty_title(base_url, headers):
    create_resp = requests.post(f"{base_url}/api-v2/projects",
                                headers=headers, json={
        "title": generate_unique_project_name(),
        "users": {
            "10e6c06d-a00b-4e3a-8fee-d57417921ffa": "worker"
        }
    })
    project_id = create_resp.json()["id"]

    update_resp = requests.put(f"{base_url}/api-v2/projects/{project_id}",
                               headers=headers, json={
        "title": "",
        "deleted": True,
        "users": {
            "10e6c06d-a00b-4e3a-8fee-d57417921ffa": "worker"
        }
    })

    assert update_resp.status_code == 400
    data = update_resp.json()
    assert data["error"] == "Bad Request"
    assert "title should not be empty" in data.get("message", [])

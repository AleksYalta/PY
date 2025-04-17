import requests
from utils import generate_unique_project_name


def test_get_project_success(base_url, headers):
    create_resp = requests.post(f"{base_url}/api-v2/projects",
                                headers=headers, json={
        "title": generate_unique_project_name(),
        "users": {
            "10e6c06d-a00b-4e3a-8fee-d57417921ffa": "worker"
        }
    })
    project_id = create_resp.json()["id"]

    get_resp = requests.get(f"{base_url}/api-v2/projects/{project_id}",
                            headers=headers)
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["id"] == project_id
    assert "title" in data
    assert "users" in data

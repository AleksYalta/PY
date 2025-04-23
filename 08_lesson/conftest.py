import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://api.yougile.com"


@pytest.fixture(scope="session")
def headers():
    token = \
        "XceV1cENTKSt6G0EtNaIDMRJMDzFN5JpFG5CgqvtUwB9ldEtIGWZmm0pt4ocGQoB"
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

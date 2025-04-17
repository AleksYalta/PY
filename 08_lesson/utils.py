import uuid


def generate_unique_project_name():
    return f"ГосУслуги_{uuid.uuid4().hex[:6]}"

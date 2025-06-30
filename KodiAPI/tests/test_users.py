import json
from utils.api_helpers import get_user_by_id
from utils.api_helpers import create_post
from jsonschema import validate
from pathlib import Path


def test_get_user_by_id():
    response = get_user_by_id(1)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "username" in data
    assert "email" in data


def test_get_user_not_found():
    response = get_user_by_id(9999)

    assert response.status_code == 404


def test_create_post():
    response = create_post(
        user_id=1,
        title="Sample API post",
        body="Automated test content created for validation purposes"
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Sample API post"
    assert data["body"] == "Automated test content created for validation purposes"
    assert data["userId"] == 1
    assert "id" in data


def test_user_response_schema():
    response = get_user_by_id(1)
    data = response.json()

    # Load the schema

    schema_path = Path(__file__).parent.parent / "schemas" / "user_schema.json"

    with open(schema_path) as f:
        schema = json.load(f)

    # Validate the response

    validate(instance=data, schema=schema)

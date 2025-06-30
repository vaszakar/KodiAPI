import json
from jsonschema import validate
from pathlib import Path
from utils.api_helpers import get_post_by_id

def test_post_response_schema():
    response = get_post_by_id(1)
    data = response.json()

    schema_path = Path(__file__).parent.parent / "schemas" / "post_schema.json"
    with open(schema_path) as f:
        schema = json.load(f)

    validate(instance=data, schema=schema)

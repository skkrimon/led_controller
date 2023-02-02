import json
from jsonschema import validate

SCHEMA = {
    "type": "object",
    "properties": {
        "program": {"type": "string"},
        "r": {"type": ["number", "null"]},
        "g": {"type": ["number", "null"]},
        "b": {"type": ["number", "null"]}
    }
}

def json_validator(message):
    validate(instance=message, schema=SCHEMA)
"""Test the argument schema"""
from jsonschema import Draft7Validator, RefResolver, ValidationError
import pytest
import json
import os


schema_path = os.path.join(os.path.dirname(__file__), '..', 'schemas', )


@pytest.fixture
def schema():
    with open(os.path.join(schema_path, 'servable', 'argument_type.json')) as fp:
        return json.load(fp)


@pytest.fixture
def validator(schema):
    return Draft7Validator(schema, resolver=RefResolver('file:///{}/'.format(schema_path), schema))


def test_files(validator: Draft7Validator):
    # Valid Schemas
    validator.validate({'type': 'file'})
    validator.validate({'type': 'file', 'file_types': ['text/csv']})
    validator.validate({'type': 'list', 'item_type': {'type': 'file'}})
    validator.validate({'type': 'list', 'item_type': {'type': 'file', 'file_types': ['test/csv']}})
    validator.validate({'type': 'tuple',
                        'element_types': [
                            {'type': 'file', 'file_types': ['test/csv']},
                            {'type': 'list', 'item_type': {'type': 'file'}}
                        ]})

    # Invalid schema: List of list of files
    with pytest.raises(ValidationError):
        validator.validate({'type': 'list', 'item_type': {'type': 'list', 'item_type': {'type': 'file'}}})

    # Invalid schema: Non-list collection of files
    with pytest.raises(ValidationError):
        validator.validate({'type': 'dict', 'properties': {"a": {'type': 'files'}}})

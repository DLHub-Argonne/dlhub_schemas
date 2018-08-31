from jsonschema import Draft4Validator, RefResolver
import jsonref
import glob
import os

# Find all the schemas
schema_path = os.path.abspath('schemas')
schemas = glob.glob('{}/**/*.json'.format(schema_path), recursive=True)

# Loop through to make sure they are all valid
for schema in schemas:
    print('Checking {}...'.format(os.path.relpath(schema, '.')), end="")

    # Load in the schema
    with open(schema) as fp:
        schema = jsonref.load(fp, base_uri='file:///{}/'.format(schema_path))

    # Pull in the references
    Draft4Validator.check_schema(schema)
    print('OK')

from jsonschema import Draft4Validator
import glob
import json

# Find all the schemas
schemas = glob.glob('schemas/**/*.json', recursive=True)

# Loop through to make sure they are all valid
for schema in schemas:
    print('Checking {}...'.format(schema), end="")
    with open(schema) as fp:
        schema = json.load(fp)
        Draft4Validator.check_schema(schema)
    print('OK')

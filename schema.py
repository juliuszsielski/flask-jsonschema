import json
# import copy

import jsonref
from dataclasses_jsonschema import JsonSchemaMixin
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class A(JsonSchemaMixin):
    text: str
    number: int


@dataclass_json
@dataclass
class B(JsonSchemaMixin):
    test: A


jsonref_schema = jsonref.loads(json.dumps(B.json_schema()))
# test_model = api.schema_model('Test model', copy.deepcopy(jsonref_schema))
# print(test_model)

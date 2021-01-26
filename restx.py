import copy

from flask_restx import Resource, Api

import schema as sch


api = Api()


resource_fields = api.schema_model('Test model', copy.deepcopy(sch.jsonref_schema))


@api.route('/hello')
class HelloWorld(Resource):
    @api.expect(resource_fields, validate=True)
    def post(self):
        return {'hello': 'world'}

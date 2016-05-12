from flask.ext.restful import Resource

class EmployeeApi(Resource):
    def get(self):
        return {'hello':'employee'}
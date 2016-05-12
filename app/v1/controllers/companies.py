from flask.ext.restful import Resource

class CompanyApi(Resource):
    def get(self):
        return {'hello':'company'}
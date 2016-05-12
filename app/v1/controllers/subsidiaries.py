from flask.ext.restful import Resource

class SubsidiaryApi(Resource):
    def get(self):
        return {'hello':'subsidiary'}
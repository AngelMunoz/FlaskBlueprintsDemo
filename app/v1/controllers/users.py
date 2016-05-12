from flask.ext.restful import Resource

class UserApi(Resource):
    def get(self):
        return {'hello':'User'}
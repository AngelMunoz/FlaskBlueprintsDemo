from app import api
from flask.ext.restful import Resource
from app.v1.controllers.users import UserApi
from app.v1.controllers.companies import CompanyApi
from app.v1.controllers.subsidiaries import SubsidiaryApi
from app.v1.controllers.employees import EmployeeApi

apiv1 = Blueprint('apiv1', __name__)              




api.add_resource(UserApi, '/api/v1/users/')
api.add_resource(CompanyApi, '/api/v1/companies/')
api.add_resource(SubsidiaryApi, '/api/v1/subsidiaries/')
api.add_resource(EmployeeApi, '/api/v1/employees/')
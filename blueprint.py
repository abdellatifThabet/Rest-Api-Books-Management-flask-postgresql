from flask import Blueprint
from flask_restx import Api
from flask_restx import Namespace


# init the api doc
# for more details visit: https://flask-restx.readthedocs.io/en/latest/
blueprint_v1 = Blueprint('api', __name__, url_prefix='/api')


app_ns = Namespace('External', ordered=True, validate=True, path='/app',
                   description='Those services are for scrapping the data')

api_v1 = Api(blueprint_v1, version='1.0', title='Restful api to scrap and manage data', ordered=True, validate=True,
             description='scrap and manage data in postgresql database',
             )

api_v1.add_namespace(app_ns)

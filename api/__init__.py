from flask_restful import Api
from app import flask_app_instance
from User import User

rest_server = Api(flask_app_instance)
rest_server.add_resource(User, '/api/python/user')

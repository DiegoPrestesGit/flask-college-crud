from flask_restful import Resource
import logging as logger
from .database import get_all_users

class User(Resource):
    def get(self):
        get_all_users()
        return {"message": "get"}, 200

    def post(self):
        logger.debug("inside create method")
        return {"message": "post"}, 201

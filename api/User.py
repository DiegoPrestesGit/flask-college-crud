from flask_restful import Resource
import logging as logger
from .database import get_all_users


class User(Resource):
    def get(self):
        users = get_all_users()
        return users, 200

    def post(self):
        logger.debug("inside create method")
        return {"message": "post"}, 201

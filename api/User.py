from flask_restful import Resource
import logging as logger
from .database import get_all_users, create_user
import requests


class User(Resource):
    def get(self):
        users = get_all_users()
        return users, 200

    def post(self):
        create_user()
        return {"message": "post"}, 201

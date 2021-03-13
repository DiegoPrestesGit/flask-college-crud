from flask_restful import Resource
import logging as logger


class User(Resource):
    def get(self):
        logger.debug("inside get method")
        return { "message": "get" }, 200

    def post(self):
        logger.debug("inside create method")
        return { "message": "post" }, 201

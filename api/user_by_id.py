from flask_restful import Resource
import logging as logger


class UserById(Resource):
    def get(self, user_id):
        logger.debug("inside get method")
        return {"message": user_id}, 200

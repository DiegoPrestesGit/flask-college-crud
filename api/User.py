from flask_restful import Resource
import logging as logger

class User():
    def get_user(self):
        logger.debug("inside get method")
        pass
    
    def create_user(self):
        logger.debug("inside create method")
        pass

    def get_all_users(self):
        logger.debug("inside get ALL method")
        pass

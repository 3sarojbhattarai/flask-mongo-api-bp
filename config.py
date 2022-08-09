import os
import logging
from dotenv import load_dotenv

load_dotenv()


class Config(object):

    # General
    DEBUG = False
    TESTING = False
    TIMEZONE = "US/Eastern"

    # Database
    MONGO_HOSTNAME = "localhost"
    MONGO_PORT = 27017
    MONGO_AUTH_DATABASE = ""
    MONGO_AUTH_USERNAME = ""
    MONGO_AUTH_PASSWORD = ""
    MONGO_APP_DATABASE = "flask-mongo-api-bp"

    # Secret Key
    SECRET_KEY = "BAD_SECRET_KEY"

    # API settings
    API_PAGINATION_PER_PAGE = 10

    # --------- Logging ---------
    if not os.path.exists("./logs/"):
        os.makedirs("./logs/")
    if not os.path.exists("./logs/trace.log"):
        open("./logs/trace.log", "x")

    logging.basicConfig(
        level=os.getenv("LOGLEVEL", "DEBUG"),
        handlers=[logging.FileHandler("./logs/trace.log"), logging.StreamHandler()],
    )


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    # production config
    pass
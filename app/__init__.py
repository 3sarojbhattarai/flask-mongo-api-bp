from flask import Flask, jsonify
from pymongo import MongoClient
from config import DevelopmentConfig
from flask_jwt_extended import JWTManager

####################################
### Configuration           ########
####################################

client = MongoClient(DevelopmentConfig.MONGO_HOSTNAME, DevelopmentConfig.MONGO_PORT)
database = client[DevelopmentConfig.MONGO_APP_DATABASE]

def create_app():

    # Flask Config
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    initialize_app(app)
    register_blueprint(app)
    index_route(app)

    return app

def initialize_app(app):
  jwt = JWTManager(app)

def register_blueprint(app):
    # Import Routes
    from app.api.users.routes import user_blueprint
    from app.api.stocks.routes import stocks_blueprint

    #Register blueprint
    app.register_blueprint(user_blueprint, url_prefix="/api/v1/user")
    app.register_blueprint(stocks_blueprint, url_prefix="/api/v1/stock")


def index_route(app):

  @app.route("/")
  def index():
    return jsonify({ "status": "Online" }), 200


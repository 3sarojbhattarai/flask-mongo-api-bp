from app.models import stocks_collection
import hashlib
from flask import request, jsonify, Blueprint

stocks_blueprint = Blueprint("stocks", __name__)


@stocks_blueprint.route("/add_stock", methods=["POST"])
def register():

    new_stock = request.get_json()
	
    try:
        stocks_collection.insert_one(new_stock)
        return jsonify({"msg": "Stock created successfully"}), 201

    except Exception as ex:
        print(ex)
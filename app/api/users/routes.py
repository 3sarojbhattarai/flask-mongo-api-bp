from app.models import users_collection
import hashlib
from flask import request, jsonify, Blueprint
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/signup", methods=["POST"])
def register():

    new_user = request.get_json()
    new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest()

    doc = users_collection.find_one(
        {"username": new_user["username"]}
    )  
	
	# check if user exist
    if not doc:
        users_collection.insert_one(new_user)
        return jsonify({"msg": "User created successfully"}), 201
    else:
        return jsonify({"msg": "Username already exists"}), 409


@user_blueprint.route("/login", methods=["POST"])
def login():

    login_details = request.get_json()
    user_from_db = users_collection.find_one(
        {"username": login_details["username"]}
    ) 
	
	# search for user in database
    if user_from_db:
        encrpted_password = hashlib.sha256(login_details["password"].encode("utf-8")).hexdigest()

        if encrpted_password == user_from_db["password"]:
            access_token = create_access_token(identity=user_from_db["username"])  
			
			# create jwt token
            return jsonify(access_token=access_token), 200

    return jsonify({"msg": "The username or password is incorrect"}), 401


@user_blueprint.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity()

    user_from_db = users_collection.find_one({"username": current_user})

    if user_from_db:
        del (
            user_from_db["_id"],
            user_from_db["password"],
        )  # delete data we don't want to return
        return jsonify({"profile": user_from_db}), 200
    else:
        return jsonify({"msg": "Profile not found"}), 404

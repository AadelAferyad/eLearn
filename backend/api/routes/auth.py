#!/usr/bin/python3
from api.routes import auth_bp
from flask import jsonify, request
from models import storage
from flask_jwt_extended import create_access_token, create_refresh_token


@auth_bp.route('login', methods=['POST'], strict_slashes=False)
def login():
    """ login and username """
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Empty data"}), 400
    user = storage.check_username(data.get('username', None))
    if user and (user.check_password(data.get('password', None))):
        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)
        return jsonify({
                "message": "Logged In",
                "tokens": {
                    "access":access_token,
                    "refresh":refresh_token
                }
                }), 200
    return jsonify({"error": "Invalid Username or Password"}), 400

#logout not implemanted yet!


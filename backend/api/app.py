#!/usr/bin/python3
from flask import Flask, jsonify
from models import storage
from dotenv import load_dotenv
from api.routes import auth_bp
from api.routes import view_bp
from os import getenv
from flask_jwt_extended import JWTManager
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = getenv('FLASK_JWT_KEY')
jwt = JWTManager()
jwt.init_app(app)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


#------flask app register blueprints -----
app.register_blueprint(auth_bp, url_prefix='/api/v1')
app.register_blueprint(view_bp, url_prefix='/api/v1')
@app.teardown_appcontext
def close(ctx):
    """  """
    storage.close()

#------ jwt load user --------
@jwt.user_lookup_loader
def get_user(_jwt_headers, jwt_data):
    """
       get authonticated user from database
    """
    identity = jwt_data['sub']
    return storage.check_username(identity)

#------ jwt claims -----------
@jwt.additional_claims_loader
def additional_claims(identity):
    """ add ac """
    user = storage.check_username(identity)
    if user and user.director:
        role = 'director'
    elif user and user.teacher:
        role = "teacher"
    elif user and user.student:
        role = "student"
    else:
        role = None

    return {'role': role}


#------jwt error handlers-----
@jwt.expired_token_loader
def expired_token(jwt_header, jwt_data):
    """
        when sending request with an expired token
        this function will be trigger and throw this json error message
    """
    return jsonify({"message": "Token has expired", "error": "token_expired"}), 401


@jwt.invalid_token_loader
def invalid_token(error):
    """
        when sending request with an invalid token (token that is not from this api)
        this function will be trigger and throw this json error message
    """
    return jsonify({"message": "Segnature verification failed", "error": "invalid_token"}), 401


@jwt.unauthorized_loader
def missing_token(error):
    """
        when sending request without token (authorization headers)
        this function will be trigger and throw this json error message
    """
    return jsonify({"message": "Request doesn't contain a valid token", "error": "authorizaton_header"}), 401



if __name__ == "__main__":

    if getenv("HOST"):
        host = getenv("HOST")
    else:
        host = "0.0.0.0"
    if getenv("PORT"):
        port = int(getenv("PORT"))
    else:
        port = 5000

    app.run(host=host, port=port, threaded=True, debug=True)

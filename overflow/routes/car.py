from overflow import app, jwt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

# get additional functions
from overflow.others.user import user_exists
from overflow.others.utils import get

@app.route("/add/vehicle")
@jwt_required
def add_car():
    user_param = get("email")
    if user_exists(user_param):
        pass
    pass


@app.route('/edit/vehicle')
def edit_car():
    pass

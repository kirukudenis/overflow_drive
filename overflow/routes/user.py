from overflow import app, jwt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from ..others.user import signup,login
from ..others.utils import get


@app.route('/user/login')
def user_login_():
    param = get("param")
    password = get("password")

    if not param:
        return jsonify({"msg": "Missing username/Email/Phone parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    try:
        final = login(param,password)
        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=param)
    except Exception as e:
        print(e)
        return jsonify({"msg": "Bad username or password"}), 401
    return jsonify(access_token=access_token), 200


@app.route("/user/signup",methods=["POST"])
def signup_():
    try :
        firstname = get("firstname")
        lastname = get("lastname")
        email = get("email")
        phone = get("phone")
        type_ = get("type")
        password = get("password")
    except KeyError as e:
        print(str(e))
        return jsonify({"msg":str(e)})
    return jsonify(signup(firstname,lastname,email,phone,type_,password))

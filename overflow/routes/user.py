from overflow import app, jwt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from ..others.user import signup, login
from ..others.utils import get, response


@app.route('/user/login', methods=["POST"])
def user_login_():
    try:
        # global param,password
        param = get("email_or_username")
        password = get("password")
        try:
            final = login(param, password)
            if final:
                # Identity can be any data that is json serializable
                access_token = create_access_token(identity=final["email"])
                return response(access_token, 200)
            else:
                return response("Error! Bad Email Password Combination", 404)
        except Exception as e:
            return response("Bad username or password", 401)
    except Exception as e:
        return response(e, 500)


@app.route("/user/signup", methods=["POST"])
def signup_():
    try:
        firstname = get("firstname")
        lastname = get("lastname")
        email = get("email")
        phone = get("phone")
        type_ = get("type")
        password = get("password")
        return jsonify(signup(firstname, lastname, email, phone, type_, password))
    except Exception as e:
        # return jsonify({"msg": str(e)})
        return response(e, 500)
    # return jsonify(signup(firstname, lastname, email, phone, type_, password))

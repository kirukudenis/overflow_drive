from flask import jsonify,session
from flask_jwt_extended import create_access_token

from overflow import app
from overflow.others.user import signup, login, generate_user_token, get_token, send_code
from overflow.others.utils import get, response
from overflow.others.vehicle import  get_fare


@app.route('/user/login', methods=["POST"])
def user_login_():
    # set some session variable
    session["username"] = "denis"
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
        except Exception:
            return response("Bad username or password", 401)
    except Exception as e:
        return response(e, 500)


@app.route("/user/signup", methods=["POST"])
def signup_():
    print(session.get("username"))
    try:
        firstname = get("firstname")
        lastname = get("lastname")
        email = get("email")
        phone = get("phone")
        type_ = get("type")
        password = get("password")
        return jsonify(signup(firstname, lastname, email, phone, type_, password))
    except Exception as e:
        return response(e, 500)


@app.route('/user/password/reset/token/get', methods=['POST'])
def reset_password():
    try:
        user = get("param")
        return generate_user_token(user)
    except Exception as e:
        return response(e, 500)


@app.route("/user/password/reset/confirm", methods=["POST"])
def reset_token():
    # reset token
    try:
        param = get("param")
        lookup = get_token(param)
        return jsonify(lookup)
    except Exception as e:
        return response(e, 500)


@app.route('/user/password/resend/code', methods=["POST"])
def resend_code():
    # resend code
    try:
        param = get("param")
        lookup = get_token(param)
        if lookup:
            return send_code(lookup["code"], lookup["email"])
        else:
            return response("Error! Code Does Not exist", 404)
    except Exception as e:
        return response(e, 500)
    # check if code is in db for the suer sthat is not used
    pass


@app.route("/user/password/reset", methods=["POST"])
def reset_final():
    # password
    # confirm_password
    pass


@app.route("/user/pay/fare",methods=["POST"])
def pay_fare():


    pass



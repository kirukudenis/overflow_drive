from overflow.models.user import User, UserSchema
from werkzeug.security import generate_password_hash, check_password_hash
import re
from overflow import db

# adding the schame init
user_schema = UserSchema()
users_schema = UserSchema(many=True)


def signup(firstname, lastname, email, phone, type, password):
    """
    :param firstname:
    :param lastname:
    :param email:
    :param phone:
    :param type:
    :param password:
    :return dict:
    """
    if verify_phone(phone):
        password = generate_password_hash(password)
        lookup = User(firstname, lastname, email, phone, int(type), password)
        db.session.add(lookup)
        db.session.commit()
        if user_schema.dump(lookup):
            final = success("user Added SuccessFully")
        else:
            final = error("User Not added")
    else:
        final = error("Phone Not valid")
    return final


def login(param, password):
    if validate_email(param):
        # user login via username
        lookup = User.query.filter_by(email=param).first()
        user_data = user_schema.dump(lookup)
        if user_data:
            final = user_data if check_password_hash(user_data["password"],password) else None
        else:
            raise Exception(error("User Does Not Exists"))
    elif verify_phone(param):
        # verify phone
        lookup = User.query.filter_by(phone=param).first()
        user_data = user_schema.dump(lookup)
        if user_data:
            final = user_data if check_password_hash(user_data["password"],password) else None
        else:
            raise Exception(error("User Does Not Exists"))
    else:
        # loggin via username
        lookup = User.query.filter_by(email=param).first()
        user_data = user_schema.dump(lookup)
        if user_data:
            final = user_data if check_password_hash(user_data["password"],password) else None
        else:
            raise Exception(error("User Does Not Exists"))
    return final


def user_exists(param):
    lookup = User.query.get(param) or User.query.filter_by(email=param).first() or User.query.filter_by(
        username=param).first()
    return users_schema.dump(lookup)


def validate_email(email):
    regex = re.compile(r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,'
                       r'3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
    return re.match(regex, email)


def error(message):
    return {"status": False, "msg": message}


def success(message):
    return {"status": True, "msg": message}


def verify_phone(number):
    """
    :param number:
    :return:
    """
    regex = re.compile(r'^[+]*[(]?[0-9]{1,4}[)]?[-\s\./0-9]*$', re.IGNORECASE)
    return re.match(regex, number)

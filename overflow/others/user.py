from overflow.models.user import User, UserSchema
from werkzeug.security import generate_password_hash, check_password_hash
import re
from overflow import db
from flask_sqlalchemy import sqlalchemy
import secrets
import random
from ..others.utils import message,error,success


# adding the schame init
user_schema = UserSchema()
users_schema = UserSchema(many=True)


def signup(firstname, lastname, email, phone, type, password):
    if verify_phone(phone):
        try:
            if not  phone_exists(phone):
                if validate_email(email):
                    password = generate_password_hash(password)
                    lookup = User(random.getrandbits(24),firstname, lastname, email, phone, int(type), password)
                    db.session.add(lookup)
                    db.session.commit()
                else:
                    return {"status" : None,"msg" : "Email Not valid"}
            else:
                return {"status":None,"msg":"User Phone Exists"}

        except sqlalchemy.exc.DatabaseError as e:
            return {"msg":str(e)}

        if user_schema.dump(lookup):
            final = success("user Added SuccessFully")
        else:
            final = error("User Not added")
    else:
        final = error("Phone Not valid")
    return final


def login(param, password):
    if validate_email(param):
        lookup = User.query.filter_by(email=param).first()
        user_data = user_schema.dump(lookup)
        if user_data:
            final = user_data if check_password_hash(user_data["password"],password) else None
        else:
            raise Exception(message("User Does Not Exists"))
    elif verify_phone(param):
        # verify phone
        lookup = User.query.filter_by(phone=param).first()
        user_data = user_schema.dump(lookup)
        if user_data:
            final = user_data if check_password_hash(user_data["password"],password) else None
        else:
            raise Exception(message("User Does Not Exists"))
    else:
        # loggin via username
        lookup = User.query.filter_by(email=param).first()
        user_data = user_schema.dump(lookup)
        if user_data:
            final = user_data if check_password_hash(user_data["password"],password) else None
        else:
            raise Exception(message("User Does Not Exists"))
    return final


def user_exists(param):
    lookup = User.query.filter_by(email=param).first() or User.query.get(param)
    final = user_schema.dump(lookup)
    return final


def validate_email(email):
    regex = re.compile(r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,'
                       r'3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
    return re.match(regex, email)



def verify_phone(number):
    regex = re.compile(r'^[+]*[(]?[0-9]{1,4}[)]?[-\s\./0-9]*$', re.IGNORECASE)
    return re.match(regex, number)


def random_four():
    rand = random.getrandbits(24)
    numbers = str(rand)
    final = [numbers[i:i+4] for i in range(0, len(numbers), 4)]

    return final


def phone_exists(phone):
    lookup = User.query.filter_by(phone=phone).first()
    return user_schema.dump(lookup)


# def
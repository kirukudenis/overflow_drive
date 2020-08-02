from flask import Flask
import secrets
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from datetime import timedelta, datetime
# from flask_session import Session
# import flask
# loading the dot env module
from dotenv import load_dotenv

path = f"{os.getcwd()}/.env"
# setting the enviroment variables
load_dotenv(dotenv_path=path)

db_pass = os.getenv('DBPASS')

# __init__ the app
app = Flask(__name__)

# secret = secrets.token_urlsafe(48)
# app.secret_key = secret
# flask.Flask.secret_key = secret

# adding JWT TO THE APP
jwt = JWTManager(app)

# setting sql_alchemy database consts
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://root:{db_pass}@localhost:3306/overflow"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "denis"

# # session config
# SESSION_SQLALCHEMY = "sqlalchemy"
# SESSION_SQLALCHEMY_TABLE = "sessions"
# app.config.from_object(__name__)
#
# #
# # #init session
# Session(app)

# set some sesson variable
# session["username"] = "denis"

# setting the key for JWT
app.config["JWT_SECRET_KEY"] = secrets.token_hex(16)

# setting JWT expiry time
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=5)

# adding marshmallow
ma = Marshmallow(app)

# adding the database support
db = SQLAlchemy(app)

# flask migrate
migrate = Migrate(app, db)

# for blacklist tokens
blacklist = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


from overflow.routes import vehicle, callback, user
from overflow.models import user, vehicle, payment

from flask import Flask
import secrets
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from datetime import timedelta, datetime

# __init__ the app
app = Flask(__name__)

# setting the key for JWT
app.config["JWT_SECRET_KEY"] = secrets.token_hex(16)

# setting sql_alchemy database consts
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://root:{os.getenv('DBPASS')}@localhost:3306/overflow"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# setting JWT expiry time
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=5)


# adding JWT TO THE APP
jwt = JWTManager(app)

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


from overflow.routes import user, car
from overflow.models import user, car, payment

from flask import Flask
import secrets
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# __init__ the app
app = Flask(__name__)

# setting the key for JWT
app.config["JWT_SECRET_KEY"] = secrets.token_hex(16)

# setting sql_alchemy database consts
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost:3306/overflow"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# adding JWT TO THE APP
jwt = JWTManager(app)

# adding marshmallow
ma = Marshmallow(app)

# adding the database support
db = SQLAlchemy(app)

# flask migrate
migrate = Migrate(app, db)

from overflow.routes import user

from overflow import ma, db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), primary_key=True, nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(length=255), nullable=True)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String(length=255), nullable=True)
    type = db.Column(db.Integer, nullable=False, default=0)
    active = db.Column(db.Boolean)

    def __init__(self, id, firstname, lastname, email, phone, type_, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.type = type_
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","firtsname", "lastname", "email", "phone", "type", "password")


class PasswordToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("user.id"), nullable=False)
    token = db.Column(db.String(length=250), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    date_added = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, user, token):
        self.user_id = user
        self.token = token


class PasswordTokenSchema(ma.Schema):
    class Meta:
        fields = ("id", "user", "token", "active", "date_added")

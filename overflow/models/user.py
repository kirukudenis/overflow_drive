from overflow import ma, db, migrate
import secrets


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    firstname = db.Column(db.String(100), primary_key=True, nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(length=255), nullable=True)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String(length=255), nullable=True)
    type = db.Column(db.Integer, nullable=False, default=0)
    active = db.Column(db.Boolean)

    def __init__(self, firstname, lastname, email, phone, type_, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.type = type_
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ("firtsname", "lastname", "email", "phone", "type", "password")

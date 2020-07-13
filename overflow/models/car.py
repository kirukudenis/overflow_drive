from overflow import ma, db, migrate
import secrets
from .user import User


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    plate_number = db.Column(db.String(100), nullable=False, unique=True)
    fleet_id = db.Column(db.ForeignKey("fleet.id"), nullable=True)
    active = db.Column(db.Boolean)
    owner = db.Column(db.ForeignKey("user.id"))

    def __init__(self, plate_number, active, owner):
        self.plate_number = plate_number
        self.active = active
        self.owner = owner


class CarSchema(ma.Schema):
    class Meta:
        fields = ("id", "platenumber", "fleet_id", "active")


class Fleet(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(length=250), nullable=False)
    route = db.Column(db.ForeignKey("route.id"), nullable=False)

    def __init__(self, name, route):
        self.name = name
        self.route = route


class FleetSchema(ma.Schema):
    class Meta:
        fields = ("name", "route")


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=255), nullable=False, unique=True)
    departure = db.Column(db.ForeignKey("stage.id"), nullable=False)
    destination = db.Column(db.ForeignKey("stage.id"), nullable=False)
    fare = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, name, deparute, destination, fare):
        self.name = name
        self.departure = deparute
        self.destination = destination
        self.fare = fare


class RouteSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "departure", "destination", "fare")


class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=255), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name


class StageSchema(ma.Schema):
    class Meta:
        fieldd = ("id", "name")

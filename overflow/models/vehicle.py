from overflow import ma, db, migrate
import secrets
from .user import User


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=255), nullable=False, unique=True)
    departure = db.Column(db.ForeignKey("destination_departure.id"), nullable=False)
    destination = db.Column(db.ForeignKey("destination_departure.id"), nullable=False)
    fare = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, name, departure, destination, fare):
        self.name = name
        self.departure = departure
        self.destination = destination
        self.fare = fare


class RouteSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "departure", "destination", "fare")


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    plate_number = db.Column(db.String(100), nullable=False, unique=True)
    fleet_id = db.Column(db.ForeignKey("fleet.id"), nullable=True)
    active = db.Column(db.Boolean)
    owner = db.Column(db.ForeignKey("user.id"))
    in_service = db.Column(db.Boolean, default=True)
    route = db.Column(db.ForeignKey("route.id"), nullable=False)

    def __init__(self, plate_number, active, owner, route):
        self.plate_number = plate_number
        self.active = active
        self.owner = owner
        self.route = route


class VehicleSchema(ma.Schema):
    class Meta:
        fields = ("id", "platenumber", "fleet_id", "active", "in_service")


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


class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=255), nullable=False, unique=True)
    route = db.Column(db.ForeignKey("route.id"), nullable=False)

    def __init__(self, name, route):
        self.name = name
        self.route = route


class StageSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "route")


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=255), nullable=False)
    route = db.Column(db.ForeignKey("route.id"), nullable=False)
    car = db.Column(db.ForeignKey("car.id"), nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, name, route, car, active=True):
        self.name = name
        self.route = route
        self.car = car
        self.active = active


class GroupSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "route", "car", "active")


# adding a destination/departure
class DestinationDeparture(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=255), nullable=False)

    def __init__(self, name):
        self.name = name


class DestinationDepartureSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")

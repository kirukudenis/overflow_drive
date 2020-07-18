from overflow.models.car import Fleet, FleetSchema, Car, User, Route, Stage
from overflow.others.user import user_schema, users_schema, verify_phone, validate_email
from overflow import db
from .utils import exc
from .schema import (car_schema, cars_schema, route_schema, routes_schema, stage_schema, stages_schema)
from flask_sqlalchemy import sqlalchemy


# functions
def add_vehicle(plate_number, active, owner):
    if car_exists(plate_number):
        lookup = Car(plate_number, active, owner)
        return car_schema.dump(lookup)
    else:
        # later we could get vehicle data
        exc("Error! Vehicle already exists")


def edit_owner_email(user_id, email):
    lookup = User.query.get(user_id)
    if lookup:
        if validate_email(email):
            # email valid
            lookup.email = email
            db.session.commit()
            return user_schema.dump(lookup)
        else:
            exc("Email Is not Valid")
            # return None
    else:
        exc("User With Such Email Not Found")
        # return None


def car_exists(params):
    lookup = Car.query.get(params) or Car.query.filter_by(plate_number=params)
    return car_schema.dump(lookup)


def delete_car(plate_number):
    lookup = Car.query.filter_by(plate_number=plate_number).first()
    if lookup:
        lookup.in_service = False
        db.session.commit()
        return car_schema.dump()
    else:
        exc("Error! Car Does Not Exists")


def add_route(name, departure, destination, fare):
    lookup = Route(name, departure, destination, fare)
    try:
        db.session.add(lookup)
        db.session.add()
        return route_schema.dump(lookup)
    except sqlalchemy.exc.IntegrityError as e:
        exc(e)


def edit_fare(name, fare):
    route = route_exists(name)
    if route:
        # route_exists
        lookup = Route.query.get(route["id"])
        lookup.fare = fare
        db.sesion.commit()
        return route_schema.dump(lookup)
    else:
        exc("Error, Route Does not Exist")


def add_stage(name, route):
    if not stage_exists(name.route):
        # stage does exists
        lookup = Stage(name, route)
        return stage_schema.dump(lookup)
    else:
        exc("Error! Stage By That name exists")


def edit_stage(name, route):
    if stage_exists(name, route):
        lookup = Stage.query.filter_by(name=name).filter_by(route=route).first()
        return stage_schema.dump(lookup)
    else:
        exc("Error! Stage Does not exist")


def route_exists(name):
    lookup = Route.query.filter_by(name=name).first()
    return route_schema.dump(lookup)


def stage_exists(name, route):
    lookup = Stage.query.filter_by(name=name).filter_by(route=route).first()
    return stage_schema.dump(lookup)


def get_stage_by_name_route(name, route):
    return stage_exists(name, route)


def get_stage_by_id(id):
    lookup = Stage.query.get(id)
    return stage_schema.dump(lookup)


def get_all_stages():
    lookup = Stage.query.all()
    return stages_schema.dump(lookup)


def get_single_vehicle(plate_or_id):
    lookup = Car.query.filter_by(plate_or_id).first() or Car.query.get(plate_or_id)
    return car_schema.dump()


def get_all_vehicles():
    lookup = Car.query.all()
    return cars_schema.dump(lookup)


def get_routes_by_route(route):
    lookup = Car.query.filter_by(route=route).all()
    return cars_schema.dump(lookup)


def get_single_stage(name_id):
    lookup = Stage.query.filter_by(name=name_id).first() or Stage.query.get(name_id)
    return stage_schema.dump(lookup)


def get_all_stages():
    lookup = Stage.get.all()
    return stage_schema.dump(lookup)


def get_stages_on_route(route):
    lookup = Stage.query.filter_by(route=route).all()
    return stages_schema.dump(lookup)


def cars_through_stage(stage):
    lookup = Stage.query.filter_by(name=stage).first()
    if lookup:
        stage_data = stage_schema.dump(lookup)
        stage_route = stage_data["route"]

        # get the cars that are in the route id
        cars = Car.query.filter_by(route=stage_route).all()
        return cars_schema.dump(cars)
    else:
        exc("Error! Stage does not exist.")



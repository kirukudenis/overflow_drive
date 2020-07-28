from overflow.models.vehicle import Fleet, FleetSchema, Vehicle, User, Route, Stage, DestinationDeparture
from overflow.others.user import user_schema, users_schema, verify_phone, validate_email
from overflow import db
from .utils import exc
from .user import user_exists
from .schema import (car_schema, cars_schema, route_schema, routes_schema, stage_schema, stages_schema,
                     fleet_schema, fleets_schema, destination_departure_schema, destination_departures_schema)
from flask_sqlalchemy import sqlalchemy


# functions
def add_vehicle(plate_number, active, owner, route):
    if not car_exists(plate_number):
        if user_exists(owner):
            try:
                lookup = Vehicle(plate_number, bool(active), owner, route)
                db.session.add(lookup)
                db.session.commit()
                return car_schema.dump(lookup)
            except sqlalchemy.exc.IntegrityError as e:
                exc("Car with such plate number exists")
            except Exception as e:
                exc(e)
        else:
            exc("user Does Not Exists")
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


def edit_vehicle_route(param, route):
    if car_exists(param):
        if user_exists(param):
            if route_exists(route):
                # we have a car else
                lookup = Vehicle.query.filter_by(plate_number=param).first() or Vehicle.query.get(param)
                lookup.route = route
                db.session.commit()
                return car_schema.dump(lookup)
            else:
                exc("Error! ROute Does not Exist")
        else:
            exc("Error! Owner Deos Not Exist.")
    else:
        # the car does not exist
        exc("Error! Vehicle Does not exists")


def edit_vehicle_owner(param, owner):
    if car_exists(param):
        if user_exists(owner):
            # we have a car else
            lookup = Vehicle.query.filter_by(plate_number=param).first() or Vehicle.query.get(param)
            lookup.owner = owner
            db.session.commit()
            return car_schema.dump(lookup)
        else:
            exc("Error! Owner Deos Not Exist.")
    else:
        # the car does not exist
        exc("Error! Vehicle Does not exists")


def car_exists(params):
    lookup = Vehicle.query.filter_by(plate_number=params).first() or Vehicle.query.get(params)
    car_data = car_schema.dump(lookup)
    return car_data


def delete_car(plate_number):
    lookup = Vehicle.query.filter_by(plate_number=plate_number).first()
    if lookup:
        lookup.in_service = False
        db.session.commit()
        return car_schema.dump()
    else:
        exc("Error! Car Does Not Exists")


def add_route(name, departure, destination, fare):
    lookup = Route(name, departure, destination, fare)
    try:
        try:
            route_exists_detail(name, departure, destination)
            db.session.add(lookup)
            db.session.commit()
            return route_schema.dump(lookup)
        except Exception as e:
            exc(e)
    except sqlalchemy.exc.IntegrityError as e:
        exc(f"Error!, Record Route to {name} Exists")
    except Exception as e:
        exc(e)


def route_exists_detail(name, depart, dest):
    condition_one = Route.query.filter_by(name=name).first()
    condition_two = Route.query.filter_by(departure=depart).filter_by(destination=dest).first()
    data_one = route_schema.dump(condition_one)
    data_two = route_schema.dump(condition_two)
    if type(depart) == int and type(dest) == int:
        if condition_one:
            exc("Route with name given exists")
        elif condition_two:
            exc("Route with such Desination and Depreture Exists")
        else:
            return True
    else:
        exc("Desination/Departure Types Error")


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
    if not stage_exists(name, route):
        print("stage does not exist")
        # stage does exists
        try:
            lookup = Stage(name, route)
            db.session.add(lookup)
            db.session.commit()
            return stage_schema.dump(lookup)
        except sqlalchemy.exc.IntegrityError as e:
            exc(e)
    else:
        print("stage exists")
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
    lookup = Vehicle.query.filter_by(plate_or_id).first() or Vehicle.query.get(int(plate_or_id))
    return car_schema.dump()


def get_all_vehicles():
    lookup = Vehicle.query.all()
    return cars_schema.dump(lookup)


def get_routes_by_route(route):
    lookup = Vehicle.query.filter_by(route=route).all()
    return cars_schema.dump(lookup)


def get_single_stage(name_id):
    lookup = Stage.query.filter_by(name=name_id).first() or Stage.query.get(int(name_id))
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
        cars = Vehicle.query.filter_by(route=stage_route).all()
        return cars_schema.dump(cars)
    else:
        exc("Error! Stage does not exist.")


def is_car_infleet(param):
    if car_exists(param):
        lookup = Vehicle.query.filter_by(plate_number=param).first() or Vehicle.query.get(int(param))
        car_data = cars_schema.dump(lookup)
        route = car_data["route"]
        # getting the fleet b this name
        fleet_lookup = Fleet.query.filter_by(route=route).first()
        return fleet_schema.dump(is_car_infleet())
    else:
        exc("Error!, Car Does Not Exist.")


def add_destination(name):
    try:
        lookup = DestinationDeparture(name)
        db.session.add(lookup)
        db.session.commit()
        return destination_departure_schema.dump(lookup)
    except Exception as e:
        exc(e)


def add_fleet(name, route):
    if type(route) == int:
        if not fleet_exists(name):
            lookup = Fleet(name, route)
            db.session.add(lookup)
            db.session.commit()
            return fleet_schema.dump(lookup)
        else:
            exc("Error! Fleet by that name exists")
    else:
        exc("Error! Route param does not exist.")


def fleet_exists(param):
    lookup = Fleet.query.filter_by(name=param).first() or Fleet.query.get(int(param))
    final = fleet_schema.dump(lookup)
    print(final)
    return final


def edit_fleet_name(name, id):
    if fleet_exists(name):
        lookup = Fleet.query.get(id)
        lookup.name = name
        db.session.commit()
        return fleet_schema.dump(lookup)
    else:
        exc("Error! Fleet Does Not Exist")


def add_car_fleet(car_id, fleet):
    if fleet_exists(fleet):
        if car_exists(car_id):
            lookup = Vehicle.query.get(car_id)
            lookup.fleet_id = fleet
            db.session.commit()
            return car_schema.dump(lookup)
        else:
            exc("Error! Car Does Not Exist.")
    else:
        exc("Error! Fleet Does Not Exists")


def remove_car_fleet(car_id, fleet):
    if fleet_exists(fleet):
        if car_exists(car_id):
            lookup = Vehicle.query.get(car_id)
            lookup.fleet_id = None
            db.session.commit()
            return car_schema.dump(lookup)
        else:
            exc("Error! Car Does Not Exist.")
    else:
        exc("Error! Fleet Does Not Exists")

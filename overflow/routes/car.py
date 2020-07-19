from overflow import app, jwt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

# get additional functions
from overflow.others.user import user_exists
from overflow.others.utils import get
from overflow.others.car import (add_route, edit_fare, add_vehicle, add_stage, edit_stage, get_single_vehicle,
                                 get_all_vehicles, get_routes_by_route, get_single_stage, get_all_stages,
                                 get_stages_on_route, cars_through_stage, is_car_infleet)


@app.route("/vehicle/add", methods=["POST"])
@jwt_required
def add_car():
    user_param = get("param")
    plate_number = get("plate_number")
    active = get("active")
    owner = get("owner")

    if user_exists(user_param):
        return add_vehicle(plate_number, active, owner)
    else:
        return jsonify({"error": "User_does not exists"}), 500


@app.route('/vehicle/edit', methods=["POST"])
def edit_car():
    pass


@app.route("/vehicle/route/get", methods=["POST"])
def get_routes_by_route_():
    route = get("route")
    return get_routes_by_route(route)


'''
get a single car with either the id or the plate number
:return:
'''


@app.route("/vehicle/get/single", methods=["POST"])
def get_single_car():
    plate_or_id = get("plate_id")
    return jsonify(get_single_vehicle(plate_or_id))


@app.route('/vehicle/get/all', methods=["POST"])
def get_all_vehicles_():
    return jsonify(get_all_vehicles())


@app.route("/route/add", methods=["POST"])
def add_route_():
    name = get("name")
    departure = get("departure")
    destination = get("destination")
    fare = get("fare")
    return jsonify(add_route(name, departure, destination, fare))


@app.route("/route/fare/edit", methods=["POST"])
def edit_route_():
    name = get("name")
    fare = get("fare")
    return jsonify(edit_fare(name, fare))


@app.route("/stage/add", methods=["POST"])
def add_stage_():
    name = get("name")
    route = get("route")
    return jsonify(add_stage(name, route))


@app.route("/stage/edit", methods=["POST"])
def edit_stage_():
    name = get("name")
    route = get("route")
    return jsonify(edit_stage(name, route))


@app.route("/stage/get/single", methods=["POST"])
def get_stage():
    name_id = get("name_id")
    return get_single_stage(name_id)


@app.route("/stage/get/all", methods=["POST"])
def get_all_stages_():
    return get_all_stages()


@app.route("/stages/on/route", methods=["POST"])
def stages_on_route():
    route = get("route")
    return get_stages_on_route(route)


# these are the cars that stop wthin a give stage
@app.route("/stage/by/cars", methods=["POST"])
def cars_through_stage_():
    stage = get("stage")
    return cars_through_stage(stage)


# the fleet in which a car belong to fleet
@app.route('/fleet/car', methods=["POST"])
def which_car_fleet():
    car = get("param")
    return is_car_infleet(car)


@app.route("/fleet/add", methods=["POST"])
def add_fleet():
    pass


@app.route('/fleet/edit', methods=["POST"])
def edit_fleet():
    pass


@app.route("/fleet/cars/add", methods=["POST"])
def add_car_fleet():
    pass


@app.route("/fleet/car/remove", methods=["POST"])
def remove_car_fleet():
    pass


@app.route('/fleet/car/active', methods=["POST"])
def active_car_fleet():
    pass

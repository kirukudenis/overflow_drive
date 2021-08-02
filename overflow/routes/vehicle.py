from overflow import app, jwt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

# get additional functions
from overflow.others.user import user_exist
from overflow.others.utils import get, response
from overflow.others.vehicle import (add_route, edit_fare, add_vehicle, add_stage, edit_stage, get_single_vehicle,
                                     get_all_vehicles, get_routes_by_route, get_single_stage, get_all_stages,
                                     get_stages_on_route, cars_through_stage, is_car_infleet, add_destination,
                                     add_fleet,
                                     edit_fleet_name, add_car_fleet)


@app.route("/vehicle/add", methods=["POST"])
@jwt_required
def add_car():
    try:
        plate_number = get("plate_number")
        active = get("active")
        owner = get("owner")
        route = get("route")
        if user_exist(owner):
            try:
                final = add_vehicle(plate_number, active, owner, route)
                return final
            except Exception as e:
                return response(e, 500)
        else:
            return jsonify({"error": "User_does not exists"}), 500
    except Exception as e:
        return response(e, 500)


@app.route('/vehicle/owner/edit', methods=["POST"])
@jwt_required
def edit_car():
    try:
        plate_number = get("plate_number")
        owner = get("owner")
        if user_exist(owner):
            try:
                final = add_vehicle(plate_number, active, owner, route)
                return final
            except Exception as e:
                return response(e, 500)
        else:
            return jsonify({"error": "User_does not exists"}), 500
    except Exception as e:
        return response(e, 500)


@app.route("/vehicle/route/get", methods=["POST"])
@jwt_required
def get_routes_by_route_():
    route = get("route")
    return get_routes_by_route(route)


'''
get a single car with either the id or the plate number
:return:
'''


@app.route("/vehicle/get/single", methods=["POST"])
@jwt_required
def get_single_car():
    plate_or_id = get("plate_id")
    return jsonify(get_single_vehicle(plate_or_id))


@app.route('/vehicle/get/all', methods=["POST"])
@jwt_required
def get_all_vehicles_():
    return jsonify(get_all_vehicles())


@app.route("/route/add", methods=["POST"])
@jwt_required
def add_route_():
    try:
        name = get("name")
        departure = get("departure")
        destination = get("destination")
        fare = get("fare")
        final = add_route(name, departure, destination, fare)
        return jsonify(final)
    except Exception as e:
        return response(e, 500)


@app.route("/route/fare/edit", methods=["POST"])
@jwt_required
def edit_route_():
    name = get("name")
    fare = get("fare")
    return jsonify(edit_fare(name, fare))


@app.route("/stage/add", methods=["POST"])
@jwt_required
def add_stage_():
    try:
        name = get("name")
        route = get("route")
        return jsonify(add_stage(name, route))
    except Exception as e:
        return response(e, 500)


@app.route("/stage/edit", methods=["POST"])
@jwt_required
def edit_stage_():
    name = get("name")
    route = get("route")
    return jsonify(edit_stage(name, route))


@app.route("/stage/get/single", methods=["POST"])
@jwt_required
def get_stage():
    name_id = get("name_id")
    return get_single_stage(name_id)


@app.route("/stage/get/all", methods=["POST"])
@jwt_required
def get_all_stages_():
    return get_all_stages()


@app.route("/stages/on/route", methods=["POST"])
@jwt_required
def stages_on_route():
    route = get("route")
    return get_stages_on_route(route)


# these are the cars that stop wthin a give stage
@app.route("/stage/by/cars", methods=["POST"])
@jwt_required
def cars_through_stage_():
    stage = get("stage")
    return cars_through_stage(stage)


# the fleet in which a car belong to fleet
@app.route('/fleet/car', methods=["POST"])
@jwt_required
def which_car_fleet():
    car = get("param")
    return is_car_infleet(car)


@app.route("/fleet/add", methods=["POST"])
@jwt_required
def add_fleet_():
    # a group of cars the go to the same location
    try:
        name = get("name")
        route = get("route")
        return add_fleet(name, route)
    except Exception as e:
        return response(e, 500)


@app.route('/fleet/edit/name', methods=["PUT"])
# @jwt_required
def edit_fleet():
    try:
        name = get("name")
        id = get("id")
        return edit_fleet_name(name, id)
    except Exception as e:
        return response(e, 500)


@app.route("/fleet/car/add", methods=["PUT"])
# @jwt_required
def add_vehicle_fleet():
    try:
        fleet = get("fleet")
        car_id = get("car_id")
        return add_car_fleet(car_id, fleet)
    except Exception as e:
        return response(e, 500)


@app.route("/fleet/car/remove", methods=["POST"])
@jwt_required
def remove_vehicle_fleet():
    try:
        param = get("plate_or_id")
        param = get("fleet_id")
    except Exception as e:
        return response(e, 500)


@app.route("/departure_destination/add", methods=["POST"])
@jwt_required
def departure_destination():
    try:
        name = get("name")
        return jsonify(add_destination(name))
    except Exception as e:
        return response(e, 500)

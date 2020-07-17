from overflow import app, jwt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

# get additional functions
from overflow.others.user import user_exists
from overflow.others.utils import get
from overflow.others.car import (add_route,edit_fare,add_vehicle)


@app.route("/vehicle/add", methods=["POST"])
@jwt_required
def add_car():
    user_param = get("param")
    plate_number = get("plate_number")
    active = get("active")
    owner = get("owner")
    
    if user_exists(user_param):
        add_vehicle(plate_number,active,owner)
    pass


@app.route('/vehicle/edit', methods=["POST"])
def edit_car():

    pass


@app.route("/route/add", methods=["POST"])
def add_route():
    name = get("name")
    departure = get("departure")
    destination = get("destination")
    fare = get("fare")
    return add_route(name,departure,destination,fare)


@app.route("/route/fare/edit", methods=["POST"])
def edit_route():
    name = get("name")
    fare = get("fare")
    return edit_fare(name,fare)


@app.route("/stage/add", methods=["POST"])
def add_stage():
    pass


@app.route("/stage/edit", methods=["POST"])
def edit_stage():
    pass


@app.route("/stage/get/single", methods=["POST"])
def get_stage():
    pass


@app.route("/stage/get/all", methods=["POST"])
def get_all_stages():
    pass


# these are the cars that stop wthin a give stage
@app.route("/stage/cars",methods=["POST"])
def cars_trough_stage():
    pass


# the fleet in which a car belong to
@app.route('/fleet/cars',methods=["POST"])
def which_car_fleet():
    pass


@app.route("/fleet/add",methods=["POST"])
def add_fleet():
    pass


@app.route('/fleet/edit',methods=["POST"])
def edit_fleet():
    pass


@app.route("/fleet/cars/add",methods=["POST"])
def add_car_fleet():
    pass


@app.route("/fleet/car/remove",methods=["POST"])
def remove_car_fleet():
    pass


@app.route('/fleet/car/active',methods=["POST"])
def active_car_fleet():
    pass









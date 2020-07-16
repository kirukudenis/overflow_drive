from overflow.models.car import Fleet, FleetSchema, Car, CarSchema, User
from overflow.others.user import user_schema, users_schema, verify_phone, validate_email
from overflow import db
from .utils import exc
from .schema import car_schema


# functions
def add_vehicle(plate_number, active, owner):
    lookup = Car(plate_number, active, owner)
    return car_schema.dump(lookup)


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

from overflow.models.car import Fleet, FleetSchema, Car, CarSchema,User
from overflow.others.user import user_schema,users_schema,verify_phone,validate_email
from overflow import db
from .utils import exc

# schemas
# car
car_schema = CarSchema()
cars_schema = CarSchema(many=True)

# fleet schema
fleet_schema = FleetSchema()
fleets_schema = FleetSchema(many=True)

# functions
def add_vahicle(plate_number, active, owner):
    lookup = Car(plate_number, active, owner)
    return car_schema.dump(lookup)


def edit_ownner_email(user_id,email):
    lookup = User.query.get(user_id)
    user_data  = user_schema.dump(lookup)
    if user_data :
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

    pass

from overflow.models.car import Fleet, FleetSchema, Car, CarSchema

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


def edit_ownner():
    pass


def car_exists(params):
    lookup = Car.query.get(params) or Car.query.filter_by(plate_number=params)
    return car_schema.dump()


def delete_car():
    pass

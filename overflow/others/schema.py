from overflow.models.car import (CarSchema, FleetSchema,
                                 RouteSchema, StageSchema, DestinationDepartureSchema)
from overflow.models.user import (UserSchema, PasswordTokenSchema)
from overflow.models.payment import (MpesaSchema)

# schemas
# car
car_schema = CarSchema()
cars_schema = CarSchema(many=True)

# fleet schema
fleet_schema = FleetSchema()
fleets_schema = FleetSchema(many=True)

# route schemas
route_schema = RouteSchema()
routes_schema = RouteSchema(many=True)

# stage schema
stage_schema = StageSchema()
stages_schema = StageSchema(many=True)

# user schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# destination_departure schema
destination_departure_schema = DestinationDepartureSchema()
destination_departures_schema = DestinationDepartureSchema(many=True)

# token schema
password_reset = PasswordTokenSchema()
passwords_reset = PasswordTokenSchema(many=True)

# mpesa
mpesa_schema = MpesaSchema()
mpesas_schema = MpesaSchema(many=True)
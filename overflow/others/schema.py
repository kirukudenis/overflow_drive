from overflow.models.car import (CarSchema, FleetSchema,RouteSchema,StageSchema)
from overflow.models.user import (UserSchema)

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


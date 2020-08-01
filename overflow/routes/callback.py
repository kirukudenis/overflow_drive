import secrets
import logging

import requests
from flask import jsonify, request

from overflow import app
from overflow.models.payment import Mpesa,PaymentDump
from overflow.others.schema import mpesas_schema, mpesa_schema,payment_schema


# You may create a separate URL for every endpoint you need
@app.route('/mpesa/stkpush', methods=["POST"])
def listenb2c():
    # save the data
    request_data = request.data
    if request_data:
        # response
        decoded = request_data.decode()
        lookup = PaymentDump(decoded)
        if lookup :

            # # we are going parse the data for the database
            # # we are going to use the payments table to display;
            lookup = PaymentDump.query.filter_by(token=token).first()
            # # main object
            # payment_data = payment_schema.dump(lookup)
            #
            # print(">>>> payment data", payment_data)
            # # "start"
            #
            # # end
            # if payment_data:
            #     main = json.loads(payment_data["body"])
            #     parent = main["Body"]["stkCallback"]
            #     result_code = parent["ResultCode"]
            #     result_desc = parent["ResultDesc"]
            #     if int(result_code) == 0:
            #         print("stage 2")
            #         callback_meta = parent["CallbackMetadata"]["Item"]
            #         amount = callback_meta[0]["Value"]
            #         # succesful payment
            #         if int(amount) == 10:
            #             print("instant")
            #             # final = make_booking(service_name, start, branch_id, instant=True, user=user_id)
            #             # final = create_booking(service_name, start, branch_id, True, user_id)
            #             # sio.emit("online", final)
            #         else:
            #             print("not instant")
            #             # final = make_booking(service_name, start, branch_id, instant=False, user=user_id)
            #             # final = create_booking(service_name, start, branch_id, False, user_id)
            #             print(final)
            #             # sio.emit("online", final)
            #     else:
            #         # error with payment
            #         final = {"msg": "Error With Payment", "error": result_desc}
            # else:
            #     final = {"msg": False, "result": "Token Invalid"}
            #
            # return jsonify(final)
    else:
        logging.info("Error! payment could not be recorded")
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": secrets.token_hex()
    }
    # Send the response back to the server
    return jsonify({'message': message}), 200


@app.route("/mpesa/reversals", methods=["POST"])
def reversals():

    # save the data
    request_data = request.data
    decoded = request_data.decode()

    # define the response
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": secrets.token_hex()
    }
    # Send the response back to the server
    return jsonify({'message': message}), 200


# Change this part to reflect the API you are testing
@app.route('/mpesa/b2b/v1')
def listenb2b():
    request_data = request.data
    print(request_data)
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    }
    return message

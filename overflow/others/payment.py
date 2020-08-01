import requests
from requests.auth import HTTPBasicAuth
from base64 import b64encode
from datetime import datetime
import logging
import os
import requests
from flask import session, request
import secrets
import json
from overflow.models.payment import PaymentDump, Mpesa
from overflow.others.schema import payment_schema, payments_schema, mpesa_schema, mpesas_schema
from overflow.others.utils import exc

from overflow import db

# denis
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
link = os.getenv("DOMAIN")


def authenticate():
    """
    :return: MPESA_TOKEN -> str
    """
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    return r.text


def stk_push(amount, phonenumber):
    callback_url = f"http://{link}/mpesa/stkpush"
    token_data = authenticate()
    token = json.loads(token_data)["access_token"]
    business_shortcode = "174379"
    lipa_na_mpesapasskey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % token}
    timestamp = datetime.now().strftime("%Y%m%d%I%M%S")
    pswd = (business_shortcode + lipa_na_mpesapasskey + timestamp).encode("utf-8")
    password = b64encode(pswd).decode()
    req = {
        "BusinessShortCode": business_shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phonenumber,
        "PartyB": business_shortcode,
        "PhoneNumber": phonenumber,
        "CallBackURL": callback_url,
        "AccountReference": business_shortcode,
        "TransactionDesc": "test",
    }

    # setting the session unique ID
    session["transaction_token"] = secrets.token_urlsafe(48)

    response = requests.post(api_url, json=req, headers=headers)
    logging.info("response", response)
    return response


def paymentdump_to_mpesa(record_id):
    data = payment_exists(record_id)
    if data:
        parsed = json.loads(data)
        parent = parsed["Body"]["stkCallback"]
        merchant_request_id = parent["MerchantRequestID"]
        checkout_request_id = parent["CheckoutRequestID"]
        result_code = parent["ResultCode"]
        result_desc = parent["ResultDesc"]
        user = data["user"]
        lookup = Mpesa(merchant_request_id, checkout_request_id, result_code, result_code, user)
        # setting a unique for the database
        lookup.merchant_request_id = merchant_request_id
        lookup.checkout_request_id = checkout_request_id
        lookup.result_code = result_code
        lookup.result_desc = result_desc

        # # success details
        if int(result_code) == 0:
            # we are going to get the callbackmetadata
            callback_meta = parent["CallbackMetadata"]["Item"]
            amount = callback_meta[0]["Value"]
            receipt_number = callback_meta[1]["Value"]
            transaction_date = callback_meta[2]["Value"]
            phone_number = callback_meta[3]["Value"]

            # we are also going to add the rest of the data before commit
            lookup.amount = amount
            lookup.receipt_number = receipt_number
            lookup.transaction_date = transaction_date
            lookup.phone_number = phone_number
            db.session.add(lookup)
            db.session.commit()
        else:
            # herw we are going to se the number
            lookup.phone_number = 0000
            # here we are  just going to commit
            db.session.add(lookup)
            db.session.commit()
        # add give data back to the user
        final = mpesa_schema.dump(lookup)
    else:
        exc("Error, Payment Not Found")
        logging.info("Error! payment could not be recorded")
    return final


def payment_exists(id_):
    lookup = PaymentDump.query.get(id_)
    return payment_schema.dump(lookup)

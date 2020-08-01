from overflow import db, ma
from datetime import datetime


class Mpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=True)
    receipt_number = db.Column(db.String(255), nullable=True)
    transaction_date = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.Integer, nullable=True)
    checkout_request_id = db.Column(db.String(255), nullable=True)
    merchant_request_id = db.Column(db.String(255), nullable=True)
    result_code = db.Column(db.Integer, nullable=False)
    result_desc = db.Column(db.Text, nullable=True)
    date_added = db.Column(db.DateTime(), default=datetime.now)
    local_transactional_key = db.Column(db.String(255), nullable=False)
    user = db.Column(db.ForeignKey("user.id"), nullable=False)

    def __init__(self, merchantRequestID, checkoutRequestID, resultCode, resultDesc, user):
        self.merchant_request_id = merchantRequestID
        self.checkout_request_id = checkoutRequestID
        self.result_code = resultCode
        self.result_desc = resultDesc
        self.user = user


class MpesaSchema(ma.Schema):
    class Meta:
        fields = ("id", "amount", "receipt_number", "transaction_data", "phone_number", "checkout_request_id",
                  "merchant_request_id", "result_code", "result_desc", "date_added", "local_transactional_key")


class PaymentDump(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, data):
        self.data = data


class PaymentDumpSchema(ma.Schema):
    class Meta:
        fields = ("id", "data", "date_added")

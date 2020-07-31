from overflow.models.user import User,PasswordToken
from werkzeug.security import generate_password_hash, check_password_hash
import re
from overflow import db
from flask_sqlalchemy import sqlalchemy
import secrets
import random
import os
from ..others.utils import message,error,success,exc
from ..others.schema import (user_schema,users_schema,password_reset)
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import qrcode
from ..others.body import reset_body

def signup(firstname, lastname, email, phone, type, password):
    if verify_phone(phone):
        try:
            if not  phone_exists(phone):
                if validate_email(email):
                    password = generate_password_hash(password)
                    lookup = User(random.getrandbits(24),firstname, lastname, email, phone, int(type), password)
                    db.session.add(lookup)
                    db.session.commit()
                else:
                    return {"status" : None,"msg" : "Email Not valid"}
            else:
                return {"status":None,"msg":"User Phone Exists"}

        except sqlalchemy.exc.DatabaseError as e:
            return {"msg":str(e)}

        if user_schema.dump(lookup):
            final = success("user Added SuccessFully")
        else:
            final = error("User Not added")
    else:
        final = error("Phone Not valid")
    return final


def login(param, password):
    if validate_email(param):
        lookup = User.query.filter_by(email=param).first()
        user_data = user_schema.dump(lookup)
        if user_data:
            final = user_data if check_password_hash(user_data["password"],password) else None
        else:
            raise Exception(message("User Does Not Exists"))
    elif verify_phone(param):
        # verify phone
        lookup = User.query.filter_by(phone=param).first()
        user_data = user_schema.dump(lookup)
        if user_data:
            final = user_data if check_password_hash(user_data["password"],password) else None
        else:
            raise Exception(message("User Does Not Exists"))
    else:
        # loggin via username
        lookup = User.query.filter_by(email=param).first()
        user_data = user_schema.dump(lookup)
        if user_data:
            final = user_data if check_password_hash(user_data["password"],password) else None
        else:
            raise Exception(message("User Does Not Exists"))
    return final


def user_exists(param):
    lookup = User.query.filter_by(email=param).first() or User.query.get(param)
    final = user_schema.dump(lookup)
    return final


def validate_email(email):
    regex = re.compile(r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,'
                       r'3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
    return re.match(regex, email)


def verify_phone(number):
    regex = re.compile(r'^[+]*[(]?[0-9]{1,4}[)]?[-\s\./0-9]*$', re.IGNORECASE)
    return re.match(regex, number)


def random_four():
    rand = random.getrandbits(24)
    numbers = str(rand)
    final = [numbers[i:i+4] for i in range(0, len(numbers), 4)]

    return final

def random_four_email():
    rand = random.getrandbits(30)
    numbers = str(rand)
    final = [numbers[i:i + 4] for i in range(0, len(numbers), 4)]
    final = f"{final[0]}-{final[1]}"
    return final


def phone_exists(phone):
    lookup = User.query.filter_by(phone=phone).first()
    return user_schema.dump(lookup)


def generate_user_token(param):
    user = user_exists(param)
    if user:
        existing = PasswordToken.query.filter_by(user_id=user["id"]).first()
        if not existing :
            token = random_four_email()
            lookup = PasswordToken(user["id"], token)
            db.session.add(lookup)
            db.session.commit()
            final = password_reset.dump(lookup)
            final.update({"state":201})
        else:
            final = password_reset.dump(existing)
            final.update({"state":200})
        return final
    else:
        exc("User Does Not Exists")


def get_token(param):
    user = user_exists(param)
    if user:
        lookup = PasswordToken.query.filter_by(user_id = user["id"]).filter_by(active=True).first()
        return password_reset.dump(lookup)
    else:
        exc("Error! User Does Not Exist")


def send_code(code,email) -> str:
    user = user_exists(param)
    if user:
        return send_email(email,"Password Reset Request. Code.",reset_body(user["firstname"],get_token(user["id"])))
    else:
        exc(("Error! User Does Not  Exist"))


def send_email(_to, subject, body) -> bool:
    _from = "admin@fuprox.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = _from
    message["To"] = _to

    # Turn these into plain/html MIMEText objects
    part = MIMEText(body, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.fuprox.com", 465, context=context) as server:
        server.login(_from, "Japanitoes")
        if server.sendmail(_from, _to, message.as_string()):
            return True
        else:
            return False


def send_email_with_attachment(subject,from_,to_,body_,attachment_,bcc=""):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = from_
    message["To"] = to_
    message["Subject"] = subject
    message["Bcc"] = bcc_  # Recommended for mass emails

    if os.path.exists(attachment_) and os.path.isfile(attachment):
        # assuming the file is less that 25 megabytes

        if os.path.getsize(attachment_) < 25 * 1024 * 1024 * 1024:
            # Add body to email
            message.attach(MIMEText(body_, "plain"))

            filename = attachment_  # In same directory as script

            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()
        else:
            exc("Error! The Attachment is too large.")
    else:
        exc("Error Attachment issue. File not found")
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        return server.sendmail(sender_email, receiver_email, text)


def pay(user,route,car):
    pass

def qr(info):
    qrcode.make(info)
    return qrcode.save(f"{os.getcwd()}/overflow/statics/qr/{info}.png")

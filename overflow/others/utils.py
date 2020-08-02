from flask import request, jsonify
import json, secrets


def get(key):
    try:
        return request.json[key]
    except TypeError:
        exc("Error! {} is required.".format(key))
    except KeyError:
        exc("Error! {} is required.".format(key))


def exc(msg):
    raise Exception(msg)


def message(msg):
    return {"response": msg}


def error(msg):
    return {"status": False, "response": msg}


def success(msg):
    return {"status": True, "response": msg}


def response(msg, code):
    string = "{" + f'"response": "{str(msg)}"' + "}"
    d = json.loads(string.replace("'", "\""))
    return jsonify(d), code


def route_token():
    return str(secrets.token_hex(3)).upper()


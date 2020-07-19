from flask import request, jsonify
import json


def get(key):
    try:
        return request.json[key]
    except TypeError:
        exc("Error! {} is required.".format(key))
    except KeyError:
        exc("Error! {} is required.".format(key))


def exc(msg):
    raise Exception(msg)


def message(message):
    return {"response": message}


def response(msg, code):
    string = "{" + f'"response": "{msg}"' + "}"
    d = json.loads(string.replace("'", "\""))
    return jsonify(d),500

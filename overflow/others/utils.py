from flask import request


def get(key):
    return request.json[key]


def exc(msg):
    raise Exception(error("User Does Not Exists"))


def error(message):
    return {"status": False, "msg": message}


def success(message):
    return {"status": True, "msg": message}

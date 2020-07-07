from flask import request


def get(key):
    return request.json[key]

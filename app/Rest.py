from flask import Blueprint
from app import app, cars_cache
#from app import cars_cache
from flask import abort
from flask import request
from flask import Response
from flask import jsonify

rest_api = Blueprint('rest_api', __name__)

@rest_api.route("/")
def helloRest():
    return "Hello Rest"

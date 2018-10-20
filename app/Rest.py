from flask import Blueprint
from app import app, cars_cache
from flask import abort
from flask import request
from flask import Response
from flask import jsonify
from json import dumps, loads

rest_api = Blueprint('rest_api', __name__)

@rest_api.route("/")
def helloRest():
    return "Hello Rest"

@rest_api.route("/car/<_id>", methods=["GET"])
def car(_id):
    car = cars_cache.getCar(str(_id))
    if car is None:
        return jsonify({}), 404
    return Response(car.toJSON(), mimetype='application/json', status=200)

@rest_api.route("/cars", methods=["POST"])
def cars():
    content = request.get_json()
    if "ids" not in content:
        abort(500)
    ids = content["ids"]
    cars = cars_cache.getCars(ids)
    #Well, this is a horrible workaround... This way I can avoid making my car class serializable for now
    cars_json = dumps(list(map(loads, list(map(lambda o: o.toJSON(), cars)))))
    return Response(cars_json, mimetype='application/json', status=200)

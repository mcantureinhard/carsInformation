import redis
from app.car import Car
from app import redis_client
from json import dumps

def makeCarDict(make, model, year, capacity, picture_ids):
    carDict = {"make" : make, "model": model, "year" : year, "capacity": capacity, "picture_ids": picture_ids}
    return carDict

cars = [
makeCarDict("audi", "a3", 2017, 4, [1]),
makeCarDict("audi", "a3", 2016, 4, [2]),
makeCarDict("audi", "a3", 2015, 4, [3]),
makeCarDict("audi", "a4", 2017, 4, [4]),
makeCarDict("audi", "a4", 2016, 4, [5]),
makeCarDict("audi", "a4", 2015, 4, [6]),
makeCarDict("bmw", "M3", 2017, 4, [7]),
makeCarDict("bmw", "335i", 2017, 4, [8]),
makeCarDict("bmw", "325i", 2018, 4, [9]),
makeCarDict("bmw", "Z3", 2015, 2, [10])
]


#let's insert into redis
cars = list(map(lambda o:redis_client.hset("cars_info", o.getMake() +"_" +o.getModel()+"_"+str(o.getYear()) ,o.toJSON()), list(map(Car.from_dict, cars))))

from json import loads, dumps

class Car:
    def __init__(self, make, model, year, capacity, picture_ids):
        self.make = make
        self.model = model
        self.year = year
        self.capacity = capacity
        self.picture_ids = picture_ids
    def __repr__(self):
        return "<Make=%r, Model=%r, Year=%r, Capacity=%r>" % (self.make, self.model, self.year, self.capacity)
    @classmethod
    def from_json(class_object, json_str):
        json = loads(json_str)
        try:
            car = class_object(**json)
        except TypeError as e:
            print(e)
            return None
        return car
    @classmethod
    def from_dict(class_object, dict):
        try:
            car = class_object(**dict)
        except TypeError as e:
            print(e)
            return None
        return car
    def toJSON(self):
        return dumps(self, default=lambda o: o.__dict__, sort_keys=False)
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getYear(self):
        return self.year
    def toDict(self):
        return self.__dict__

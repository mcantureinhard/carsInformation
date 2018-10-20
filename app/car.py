from json import loads

class Car:
    def __init__(self, make, model, year, insurance, capacity, fuel_option, picture_ids):
        self.make = make
        self.model = model
        self.year = year
        self.insurance = insurance
        self.capacity = capacity
        self.fuel_option = fuel_option
        self.picture_ids = picture_ids
    @classmethod
    def from_json(class_object, json_str):
        json = loads(json_str)
        try:
            print(json)
            car = class_object(**json)
        except TypeError as e:
            print(e)
            return None
        return car

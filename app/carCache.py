from app.car import Car
#Cars don't change much and the data needed is not much
#Let's have it all live in memory
#For simplicity I won't be updating this after the initial load
#I'll use a simple dictionary composed of make_model_year

class CarCache:
    def __init__(self):
        self.cars = {}
    def insertCreate(self, key, json_data):
        #I won't be checking for collisions, there shouldn't be any anyway
        car = Car.from_json(json_data)
        if car is not None:
            self.cars[key] = car
    #I will assume to receive a list of key-value objects
    def insertBatch(self, data_list):
        for key, value in data_list.items():
            self.insertCreate(key, value)
    def getCar(self, key):
        if key in self.cars:
            return self.cars[key]
        return None
    def getCars(self, keys):
        cars = list(filter(lambda x: x is not None,list(map(self.getCar, keys))))
        #[self.getCar() for key in keys]
        return cars
    def getCarsAsDict(self, keys):
        carsDict = { key: self.cars[key].toDict() for key in list(filter(lambda x : x in self.cars, keys)) }
        return carsDict

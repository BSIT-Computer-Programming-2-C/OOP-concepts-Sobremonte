class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        return f"Car: {self.make} {self.model} with {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, make, model, cc):
        super().__init__(make, model)
        self.cc = cc

    def display_info(self):
        return f"Motorcycle: {self.make} {self.model} with {self.cc}cc engine"

def print_vehicle_info(vehicle):
    print(vehicle.display_info())

car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Yamaha", "MT-07", 689)

print_vehicle_info(car)
print_vehicle_info(motorcycle)

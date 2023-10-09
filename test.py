
from collections import namedtuple

car = namedtuple('Car', ['name', 'model', 'color', 'power'])
print(car)

class Car:
    def __init__(self, name, model, color,power):
        self.name = name
        self.model = model
        self.color = color
        self.power = power

car2 = Car("Nexia", "Daewoo", "Black", 123)
print(car2.model)
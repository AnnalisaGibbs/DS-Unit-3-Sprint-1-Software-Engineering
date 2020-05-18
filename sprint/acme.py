import random

class Product():
    def __init__(self, name = '', price = 10, weight = 20, flammability = .5, identifier = random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

if __name__ == "__main__":
    pass

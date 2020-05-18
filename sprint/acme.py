import random

class Product():
    def __init__(self, name = '', price = 10, weight = 20, flammability = .5, identifier = random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if(self.weight == 0):
            return "FUGHEDDABOUTIT"

        stealability_ratio = self.price/self.weight;

        if(stealability_ratio < .5):
            return "Not so stealable..."

        if(.5 <= stealability_ratio < 1):
            return "Kinda stealable."

        return "Very stealable!"

    def explode(self):
        explodability = self.flammability * self.weight

        if(explodability < 10):
            return "...fizzle."

        if(10 <= explodability < 50):
            return "...boom!"
        
        return "...BABOOM!!"

class BoxingGlove(Product):
    def __init__(self, name = '', price = 10, weight = 20, flammability = .5, identifier = random.randint(1000000,9999999)):
        super().__init__(name,price,weight,flammability,identifier)

    def punch(self):
        if(self.weight < 5):
            return "That tickles."
        
        if(5 <= self.weight < 15):
            return "Hey that hurt!"

        return "OUCH!"

if __name__ == "__main__":
    pass

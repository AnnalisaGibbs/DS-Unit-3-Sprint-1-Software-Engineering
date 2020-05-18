from acme import Product
from acme import BoxingGlove

prod = Product('A Cool Toy')
print('name:', prod.name)
print('price:', prod.price)
print('weight:', prod.weight)
print('flammability:', prod.flammability)
print('identifier:', prod.identifier)

print('stealable?', prod.stealability())
print('explodable?', prod.explode())

print("=========================")

glove = BoxingGlove('Punchy the Third')
print('Glove price:', glove.price)
print('Glove weight:', glove.weight)
print('Glove punch:', glove.punch())
print('Glove explode:', glove.explode())

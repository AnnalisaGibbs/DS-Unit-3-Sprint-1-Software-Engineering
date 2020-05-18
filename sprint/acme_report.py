from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products = 30):
    list = []

    for x in range(num_products):
        name = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
        list.append(Product(name, random.randint(5,100),random.randint(5,100),random.uniform(0.0,2.5)))

    return list

def inventory_report(products):
    unique_names = []
    sum_price = 0
    sum_weight = 0
    sum_flammability = 0

    for product in products:
        if(unique_names.count(product.name) == 0):
            unique_names.append(product.name)

        sum_price += product.price
        sum_weight += product.weight
        sum_flammability += product.flammability

    print("Unique product names:", len(unique_names))
    print("Average price:", sum_price/len(products))
    print("Average weight:", sum_weight/len(products))
    print("Average flammability:", sum_flammability/len(products))

if __name__ == '__main__':
    inventory_report(generate_products())



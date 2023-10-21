from database.server_methods.create import create_compound_products, create_fabric, create_implementation, create_ingredients, create_procurement, create_product
from datetime import datetime, timedelta
from database.server_methods.delete import drop_table
import random
from database.server_methods.get import get_products

product_name_list = [
    "Bread",
    "Baggutte",
    "White bread",
    "Wheat bread",
    "Rye bread",
    "Ciabatta",
    "Pita",
    "Bagel",
    "Croissant",
    "Flat bread",
    "Tortilla",
]

product_calories_by_name = {
    "Bread": 250,
    "Baggutte": 289,
    "White bread": 250,
    "Wheat bread": 265,
    "Rye bread": 226,
    "Ciabatta": 236,
    "Pita": 275,
    "Bagel": 242,
    "Croissant": 504,
    "Flat bread": 263,
    "Tortilla": 327,
}

compound_ingridients = {
    "Bread": 5,
    "Baggutte": 4,
    "White bread": 5,
    "Wheat bread": 6,
    "Rye bread": 4,
    "Ciabatta": 4,
    "Pita": 5,
    "Bagel": 7,
    "Croissant": 5,
    "Flat bread": 4,
    "Tortilla": 4,
}

def start():
    start_date = datetime.now() - timedelta(days=14)
    expiration = start_date + timedelta(days=14)
    procurement = start_date


    for i in range(1000):
        try:
            product_name =  random.choice(product_name_list)
            fabric_quantity = random.randint(0, 200)
            product_id = create_product(product_name, 100, expiration, random.randint(10, 100), product_calories_by_name[product_name])
            create_fabric(product_id, fabric_quantity, start_date, random.randint(0, fabric_quantity))
            create_implementation(product_id, random.randint(10, 100), start_date)
            compound_id = create_compound_products(product_id, compound_ingridients[product_name])
            ingredient_id = create_ingredients(compound_id, expiration, product_calories_by_name[product_name], random.randint(10, 100))
            create_procurement(ingredient_id, random.randint(10, 100), procurement, random.choice([True, False]))

        except Exception as e:
            print(e)
     

if __name__ == "__main__":
    #drop_table()
    start()
    #get_products()
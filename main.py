
from database.server_methods.create import create_compound_products, create_fabric, create_implementation, create_ingredients, create_procurement, create_product
from datetime import datetime
from database.server_methods.delete import drop_table
import random

def start():

    product_name = [
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
        "Rolls"
    ]
    for i in range(1000):
        try:
            product_id = create_product(random.choice(product_name), random.randint(10, 100), datetime.now(), random.randint(10, 100), random.randint(10, 100))
            create_fabric(product_id, random.randint(10, 100), datetime.now(), random.randint(10, 100))
            create_implementation(product_id, random.randint(10, 100), datetime.now())
            compound_id = create_compound_products(product_id, random.randint(10, 100))
            ingredient_id = create_ingredients(compound_id, datetime.now(), random.randint(10, 100), random.randint(10, 100))
            create_procurement(ingredient_id, random.randint(10, 100), datetime.now(), True)

        except Exception as e:
            print(e)
     

if __name__ == "__main__":
    drop_table()
    start()
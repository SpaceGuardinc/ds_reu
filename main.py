
from database.server_methods.create import create_compound_products, create_fabric, create_implementation, create_ingredients, create_procurement, create_product
from datetime import datetime, timedelta
from database.server_methods.delete import drop_table
import random


# import random
# from datetime import datetime, timedelta

# # Генерация случайной даты в диапазоне 1 год
# start_date = datetime.now() - timedelta(days=365)
# random_date = start_date + timedelta(days=random.randint(0, 365))

# # Прибавление 1 года к случайной дате
# new_date = random_date + timedelta(days=365)

# # Вывод результатов
# print(f"Случайная дата: {random_date}")
# print(f"Дата после добавления 1 года: {new_date}")

def start():
    start_date = datetime.now() - timedelta(days=14)
    expiration = start_date + timedelta(days=14)
    procurement = start_date
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
            product_id = create_product(random.choice(product_name), random.randint(10, 100), expiration, random.randint(10, 100), random.randint(10, 100))
            create_fabric(product_id, random.randint(10, 100), start_date, random.randint(10, 100))
            create_implementation(product_id, random.randint(10, 100), start_date)
            compound_id = create_compound_products(product_id, random.randint(10, 100))
            ingredient_id = create_ingredients(compound_id, expiration, random.randint(10, 100), random.randint(10, 100))
            create_procurement(ingredient_id, random.randint(10, 100), procurement, True)

        except Exception as e:
            print(e)
     

if __name__ == "__main__":
    drop_table()
    start()
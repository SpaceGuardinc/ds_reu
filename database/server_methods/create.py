#from .delete import delete_request
from database.main import Database
from database.models import Products, CompoundProducts, Ingredients, Procurement, Fabric, Implementation
#from .get import get_products_id, get_compound_product_id, get_ingredient_id

def create_product(name_product:str, weight_product: int, product_expiration_date: str, wholesale_price_product: int, calories_product: int):
    session = Database().session
    new_object = Products(name_product = name_product, weight_product = weight_product,
                        product_expiration_date = product_expiration_date, wholesale_price_product = wholesale_price_product, calories_product = calories_product)
    session.add(new_object)
    session.flush()
    session.commit()
    return new_object.id


def create_compound_products(product_id: int, 
                            quantity: int):
    session = Database().session
    new_object = CompoundProducts(product_id = product_id, 
                                quantity = quantity)
    session.add(new_object)
    session.flush()
    session.commit()
    return new_object.id

def create_ingredients(compound_id: int, 
                       product_expiration_date: str, 
                       calories_product: int, price: int):
    session = Database().session
    new_object = Ingredients(compound_id = compound_id, 
                            product_expiration_date = product_expiration_date,
                            calories_product = calories_product, 
                            price = price)
    session.add(new_object)
    session.flush()
    session.commit()
    return new_object.id

def create_procurement(ingredient_id: int, 
                    quantity: int, 
                    procurement_date: str, 
                    added: bool):
    session = Database().session
    session.add(Procurement(quantity = quantity, 
                            procurement_date = procurement_date, 
                            added = added,
                            ingredient_id = ingredient_id))
    session.commit()

def create_fabric(product_id: int, quantity: int, date_manufacture: str, defective: int):
    session = Database().session
    session.add(Fabric(product_id = product_id, quantity = quantity, date_manufacture = date_manufacture, defective = defective))
    session.commit()

def create_implementation(product_id: int, quantity: int, date_manufacture: str):
    session = Database().session
    session.add(Implementation(product_id = product_id, quantity = quantity, date_manufacture = date_manufacture))
    session.commit()


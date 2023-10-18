from .delete import delete_request
from ...database.main import Database
from ...database.models import Products, CompoundProducts, Ingredients, Procurement, Fabric, Implementation
from .get import get_products_id, get_compound_product_id, get_ingredient_id


def create_product(name_product:str, weight_product: str, product_expiration_date: str, whosale_price_product: str):
    session = Database().session
    session.add(Products(name_product = name_product, weight_product = weight_product, 
                        product_expiration_date = product_expiration_date, whosale_price_product = whosale_price_product))
    session.commit()

def create_compound_products(product_id: int, quantity: int, products_id: int):
    session = Database().session
    products_id = get_products_id(products_id)
    session.add(CompoundProducts(product_id = product_id, quantity = quantity))
    session.commit()

def create_ingredients(compound_id: int, product_expiration_date: str, calories_product: int, price: int,
                       compound_product_id: int):
    session = Database().session
    compound_product_id = get_compound_product_id(compound_product_id) 
    session.add(Ingredients(compound_id = compound_id, product_expiration_date = product_expiration_date,
                            calories_product = calories_product, price = price))
    session.commit()

def create_procurement(ingredient_id: int, quantity: int, procurement_date: str, added: bool):
    #products_id = get_products_id(products_id)
    session = Database().session
    ingredient_id = get_ingredient_id(ingredient_id)
    session.add(Procurement(quantity = quantity, procurement_date = procurement_date, added = added))
    session.commit()

def create_fabric(products_id: int, quantity: int, date_manufacture: str, defective: int):
    session = Database().session
    products_id = get_products_id(products_id)
    session.add(Fabric(quantity = quantity, date_manufacture = date_manufacture, defective = defective))
    session.commit()

def create_implementation(product_id: int, quantity: int, date_manufacture: str):
    session = Database().session
    products_id = get_products_id(products_id)
    session.add(Implementation(quantity = quantity, date_manufacture = date_manufacture))
    session.commit()


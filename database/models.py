from sqlalchemy import Column, Boolean, Integer, VARCHAR, ForeignKey, Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from .main import Database


"""
ref: products.id < compound_products.product_id
ref: compound_products.id < ingredients.compound_id
ref: ingredients.id - procurement.ingredient_id
ref: products.id - fabric.product_id
ref: products.id - implementation.product_id
"""

class Products(Database.BASE):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name_product = Column(VARCHAR, nullable=True)
    weight_product = Column(Integer, nullable=True)
    product_expiration_date = Column(Date, nullable=True)
    calories_product = Column(Integer, nullable=True)
    wholesale_price_product = Column(Integer, nullable=True)
    compound_products_id = relationship("CompoundProducts")
    fabric = relationship("Fabric", uselist=False, backref="products")
    implementation = relationship("Implementation", uselist=False, backref="products")


class CompoundProducts(Database.BASE):
    __tablename__ = 'compound_products'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    ingredients_id = relationship("Ingredients")

class Ingredients(Database.BASE):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    compound_id = Column(Integer, ForeignKey("compound_products.id"))
    product_expiration_date = Column(Date, nullable=True)
    calories_product = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)
    procurement = relationship("Procurement", uselist=False, backref="ingredients")

class Procurement(Database.BASE):
    __tablename__ = 'procurement'
    id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    quantity = Column(Integer, nullable=True)
    procurement_date = Column(Date, nullable=True)
    added = Column(Boolean, nullable=True)

class Fabric(Database.BASE):
    __tablename__ = 'fabric'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=True)
    date_manufacture = Column(Date, nullable=True)
    defective = Column(Integer, nullable=True)

class Implementation(Database.BASE):
    __tablename__ = 'implementation'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=True)
    date_manufacture = Column(Date, nullable=True)

def register_models():
    Database.BASE.metadata.create_all(Database().engine)


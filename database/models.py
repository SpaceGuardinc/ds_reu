from sqlalchemy import Column, Boolean, Integer, String, BIGINT, VARCHAR, BOOLEAN, ForeignKey, Date
from sqlalchemy.orm import relationship

from main import Database


class Products(Database.BASE):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name_product = Column(VARCHAR, nullable=True)
    weight_product = Column(Integer, nullable=True)
    product_expiration_date = Column(Integer, nullable=True)
    calories_product = Column(Integer, nullable=True)
    wholesale_price_product = Column(Integer, nullable=True)
    compound_product = relationship() 


class CompoundProducts(Database.BASE):
    __tablename__ = 'compound_products'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=True)
    quantity = Column(Integer, nullable=True)
    products = ForeignKey("products.id")
    ingredients = relationship(back_populates="id")

class Ingredients(Database.BASE):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    compound_id = Column(Integer, nullable=True)
    product_expiration_date = Column(Date, nullable=True)
    calories_product = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)
    compound_products = ForeignKey("compound_products.id")
    procurement = relationship(back_populates="id")

class Procurement(Database.BASE):
    __tablename__ = 'procurement'
    id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer, nullable=True)
    quantity = Column(Integer, nullable=True)
    procurement_date = Column(Date, nullable=True)
    added = Column(Boolean, nullable=True)
    ingredients = ForeignKey("ingredients.id")
    procutrment = relationship(back_populates="id")

class Fabric(Database.BASE):
    __tablename__ = 'fabric'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=True)
    quantity = Column(Integer, nullable=True)
    date_manufacture = Column(Date, nullable=True)
    defective = Column(Integer, nullable=True)
    products = ForeignKey("products.id") 
    products = relationship(back_populates="id")

class Implementation(Database.BASE):
    __tablename__ = 'implementation'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=True)
    quantity = Column(Integer, nullable=True)
    date_manufacture = Column(Integer, nullable=True)
    products = ForeignKey("products.id")
    products = relationship(back_populates="id")
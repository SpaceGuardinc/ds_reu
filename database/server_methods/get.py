from database.main import Database
from database.models import Products, CompoundProducts, Ingredients, Procurement, Fabric, Implementation
import pandas
from sqlalchemy import select
import matplotlib.pyplot as plt


def get_products():
    session = Database().session
    sql = session.query(Products.name_product, 
                        Products.weight_product, 
                        Products.product_expiration_date, 
                        Products.calories_product,
                        Products.wholesale_price_product,
                        Fabric.quantity,
                        Fabric.date_manufacture,
                        Fabric.defective,
                        Implementation.quantity,
                        Implementation.date_manufacture,
                        CompoundProducts.quantity,
                        Ingredients.product_expiration_date,
                        Ingredients.calories_product,
                        Ingredients.price,
                        Procurement.quantity,
                        Procurement.procurement_date,
                        Procurement.added).join(Fabric).join(Implementation).join(CompoundProducts).join(Ingredients).join(Procurement)
    #print(sql)
    answer_df = pandas.read_sql(
        sql=sql.statement,
        con=Database().engine
    )
    #print(answer_df)

    answer_df.plot.hist()
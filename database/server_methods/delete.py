from database.main import Database
from database.models import Products, CompoundProducts, Ingredients, Procurement, Fabric, Implementation

def drop_table():
    session = Database().session
    session.query(Procurement).delete()
    session.query(Ingredients).delete()
    session.query(CompoundProducts).delete()
    session.query(Fabric).delete()
    session.query(Implementation).delete()
    session.query(Products).delete()
    session.flush()
    session.commit()
    session.close()

# def delete_request(telegram_id) -> None:
#     session = Database().session
#     session.query(RequestGroup).filter(RequestGroup.telegram_id == int(telegram_id)).delete()
#     session.commit()


# def delete_operator(telegram_id) -> None:
#     session = Database().session
#     session.query(OperatorGroup).filter(OperatorGroup.operator_id == int(telegram_id)).delete()
#     session.commit()
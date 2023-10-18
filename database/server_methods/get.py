from sqlalchemy import exc

from ...database.main import Database
from ...database.models import AdminGroup, OperatorGroup, ModelGroup, ModelAccount, RequestGroup
from ...database.models import Products, CompoundProducts, Ingredients, Procurement, Fabric

def get_products_id(id: int) -> int:
    products_id = Database().session.query(CompoundProducts.id).where(CompoundProducts.products_id == products_id).first()
    return products_id[0]

def get_compound_product_id(id: int) -> int:
    compound_product_id = Database().session.query(Ingredients.id).where(
        Ingredients.compound_product_id == compound_product_id
        ).first()
    return compound_product_id[0]

def get_ingredient_id(id: int) -> int:
    ingredient_id = Database().session.query(Procurement.id).where(
        Procurement.ingredient_id == ingredient_id
    ).first()
    return ingredient_id[0]



# def for models
def get_all_models_to_list() -> list:
    listOfUsers = []
    index = 1
    listOfModels = Database().session.query(ModelGroup).all()
    for row in listOfModels:
        listOfUsers.append(f"{index}. {row.telegram_id} | {row.username} | {row.name}")
        index += 1
    return listOfUsers


def get_all_id_models() -> list:
    listOfId = []
    listOfModelsId = Database().session.query(ModelGroup.telegram_id).all()
    for rowInIdList in listOfModelsId:
        listOfId.append(rowInIdList.telegram_id)
    return listOfId



def get_model_id_by_telegram_id(telegram_id: int) -> int:
    model_id = Database().session.query(ModelGroup.id_model).where(ModelGroup.telegram_id == telegram_id).first()
    return model_id[0]


# def for operators
def get_operator_by_id(telegram_id: int) -> str:
    username = Database().session.query(OperatorGroup.username).where(OperatorGroup.telegram_id == int(telegram_id)).first()
    return username.username


def get_all_id_operators() -> list:
    listOfId = []
    listOfOperatorsId = Database().session.query(OperatorGroup.telegram_id).all()
    for rowInIdList in listOfOperatorsId:
        listOfId.append(rowInIdList.telegram_id)
    return listOfId


def get_all_operator() -> list:
    listOfUsers = []
    index = 1
    listOfOperators = Database().session.query(OperatorGroup).all()
    for row in listOfOperators:
        listOfUsers.append(f"{index}. {row.telegram_id} | {row.username} | {row.name}")
        index += 1
    return listOfUsers


def get_id_operator_by_telegram_id(telegram_id: int) -> int:
    operator_id = Database().session.query(OperatorGroup.id_operator).where(OperatorGroup.telegram_id == telegram_id).first()
    return operator_id[0]


# def for admins
def get_all_id_admins() -> list:
    listOfId = []
    listOfAdminsId = Database().session.query(AdminGroup.telegram_id).all()
    for rowInIdList in listOfAdminsId:
        listOfId.append(rowInIdList.telegram_id)
    return listOfId


# def for new users
def get_all_id_from_requests() -> list:
    listOfId = []
    listOfRequestsId = Database().session.query(RequestGroup.telegram_id).all()
    for row in listOfRequestsId:
        listOfId.append(row[0])
    return listOfId


def get_all_list_requests_group(group) -> list:
    listOfUsers = []
    index = 1
    listOfModels = Database().session.query(RequestGroup).where(RequestGroup.group == group).all()
    for model in listOfModels:
        listOfUsers.append(f"{index}. {model.telegram_id} | {model.username} | {model.name}")
        index += 1
    return listOfUsers


def get_all_list_requests_id_by_group(group) -> list:
    listOfIds = []
    listOfModels = Database().session.query(RequestGroup.telegram_id).where(RequestGroup.group == group).all()
    for model_id in listOfModels:
        listOfIds.append(model_id[0])
    return listOfIds


def get_user_from_request_by_id(telegram_id: int):
    data = Database().session.query(RequestGroup.username, RequestGroup.name).where(RequestGroup.telegram_id ==
                                                                                    int(telegram_id)).first()
    return data[0], data[1]

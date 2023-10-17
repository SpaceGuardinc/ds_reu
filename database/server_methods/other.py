from sqlalchemy import exc

from ...database.main import Database
from ...database.models import AdminGroup, OperatorGroup, ModelGroup, ModelAccount


def get_all_models_without_account():
    listOfUsers = []
    index = 1
    listOfModels = Database().session.query(ModelGroup).join(ModelAccount, ModelGroup.id_model == ModelAccount.id_model,
                                                             isouter=True).where(ModelAccount.id_model == None).all()
    for model in listOfModels:
        listOfUsers.append(f"{index}. {model.telegram_id} | {model.username} | {model.name}")
        index += 1
    return listOfUsers


def get_all_id_models_without_account():
    listOfIds = []
    listOfModels = Database().session.query(ModelGroup.telegram_id).\
        join(ModelAccount, ModelGroup.id_model == ModelAccount.id_model, isouter=True).\
        where(ModelAccount.id_model == None).all()
    for model_id in listOfModels:
        listOfIds.append(model_id[0])
    return listOfIds

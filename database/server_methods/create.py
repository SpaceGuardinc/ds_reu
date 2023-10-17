from .delete import delete_request
from .get import get_user_from_request_by_id, get_id_operator_by_telegram_id, get_model_id_by_telegram_id
from ...database.main import Database
from ...database.models import ModelAccount, RequestGroup, ModelGroup, OperatorGroup


def create_model_account(api_id: str, api_hash: str, phone: str, id_model: int):
    session = Database().session
    model_id = get_model_id_by_telegram_id(id_model)
    session.add(ModelAccount(api_id=api_id, api_hash=api_hash, phone=phone, auth_status=False, id_model=model_id))
    session.commit()


def create_request(telegram_id: int, username: str, name: str, group: str):
    session = Database().session
    session.add(RequestGroup(telegram_id=telegram_id, username=username, name=name, group=group))
    session.commit()


def create_operator(telegram_id: int):
    session = Database().session
    username, name = get_user_from_request_by_id(telegram_id)
    session.add(OperatorGroup(telegram_id=telegram_id, username=username, name=name))
    session.commit()
    delete_request(telegram_id)


def create_model(model_telegram_id: int, operator_telegram_id: int):
    session = Database().session
    username, name = get_user_from_request_by_id(model_telegram_id)
    operator_id = get_id_operator_by_telegram_id(operator_telegram_id)
    session.add(ModelGroup(operator_id=operator_id, telegram_id=model_telegram_id, username=username, name=name))
    session.commit()
    delete_request(model_telegram_id)

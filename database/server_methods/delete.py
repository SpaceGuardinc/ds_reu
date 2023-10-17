from ...database.main import Database
from ...database.models import AdminGroup, OperatorGroup, RequestGroup


def delete_request(telegram_id) -> None:
    session = Database().session
    session.query(RequestGroup).filter(RequestGroup.telegram_id == int(telegram_id)).delete()
    session.commit()


def delete_operator(telegram_id) -> None:
    session = Database().session
    session.query(OperatorGroup).filter(OperatorGroup.operator_id == int(telegram_id)).delete()
    session.commit()
from ...database.main import Database
from ...database.models import AdminGroup, OperatorGroup, ModelGroup, ClientGroup


def get_telegram_id_clients() -> list:
    telegram_ids = []
    answer = Database().session.query(ClientGroup.telegram_id).all()
    for row in answer:
        telegram_ids.append(row[0])
    return telegram_ids

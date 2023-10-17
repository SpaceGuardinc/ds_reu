from ...database.main import Database
from ...database.models import AdminGroup, OperatorGroup, ModelGroup, ClientGroup, ModelAccount


def create_client(telegram_id, is_self, contact, mutual_contact, deleted, bot_chat_history, bot_nochats,
                  verified, restricted, min, bot_inline_geo, support, scam, apply_min_photo, fake,
                  bot_attach_menu, premium, attach_menu_enabled, access_hash, first_name, last_name,
                  username, phone, photo, status, bot_info_version, restriction_reason, bot_inline_placeholder,
                  lang_code, emoji_status, usernames):
    session = Database().session
    session.add(ClientGroup(telegram_id=telegram_id, is_self=is_self, contact=contact,
                            mutual_contact=mutual_contact, deleted=deleted, bot_chat_history=bot_chat_history,
                            bot_nochats=bot_nochats, verified=verified, restricted=restricted, min=min,
                            bot_inline_geo=bot_inline_geo, support=support, scam=scam,
                            apply_min_photo=apply_min_photo, fake=fake, bot_attach_menu=bot_attach_menu,
                            premium=premium, attach_menu_enabled=attach_menu_enabled,
                            access_hash=access_hash, first_name=first_name, last_name=last_name,
                            username=username, phone=phone, photo=photo, status=status,
                            bot_info_version=bot_info_version, restriction_reason=restriction_reason,
                            bot_inline_placeholder=bot_inline_placeholder, lang_code=lang_code,
                            emoji_status=emoji_status, usernames=usernames))
    session.commit()




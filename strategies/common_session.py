from db.db_session import Session
from db.one.models import User
from db.two.models import Account

import constants


def create_users_combined_session():
    with Session() as session, session.begin():
        users = [User(name=f"PG#1_user_{n}") for n in range(constants.CREATE_USERS)]
        accounts = [Account(name=f"PG#2_account_{n}") for n in range(constants.CREATE_ACCOUNTS)]

        session.bulk_save_objects(users)
        session.bulk_save_objects(accounts)

        session.prepare()
        session.commit()

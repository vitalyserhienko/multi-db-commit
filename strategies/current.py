from sqlalchemy.orm import sessionmaker
from db.one.models import User
from db.two.models import Account

import constants

from db.one.db_engine import engine as db_one_engine
from db.two.db_engine import engine as db_two_engine


def create_users_current():
    postgres_one_session = sessionmaker(bind=db_one_engine, twophase=True)()
    postgres_two_session = sessionmaker(bind=db_two_engine, twophase=True)()

    postgres_one_session.begin()
    postgres_two_session.begin()

    try:
        users = [User(name=f"PG#1_user_{n}") for n in range(constants.CREATE_USERS)]
        accounts = [Account(name=f"PG#2_account_{n}") for n in range(constants.CREATE_ACCOUNTS)]

        postgres_one_session.bulk_save_objects(users)
        postgres_two_session.bulk_save_objects(accounts)

        postgres_one_session.prepare()
        postgres_two_session.prepare()

        postgres_one_session.commit()
        raise ValueError("Some error!")
        # postgres_one_session should be rolled back ?
        postgres_two_session.commit()
    except BaseException as e:
        print(f"Exception: {e}. Rolling back sessions...")
        postgres_1_session.rollback()
        postgres_2_session.rollback()

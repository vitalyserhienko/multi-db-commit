from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from db.one.models import User
from db.two.models import Account

from db.one.db_engine import engine as db_one_engine
from db.two.db_engine import engine as db_two_engine

import constants


@contextmanager
def with_session_logic():
    postgres_one_session = sessionmaker(bind=db_one_engine, twophase=True)()
    postgres_two_session = sessionmaker(bind=db_two_engine, twophase=True)()

    postgres_one_session.begin()
    postgres_two_session.begin()

    try:
        print("Before yield")
        yield postgres_one_session, postgres_two_session
        postgres_one_session.prepare()
        postgres_two_session.prepare()
        print("Before commit")
        postgres_one_session.commit()
        # raise ValueError("OMG")
        postgres_two_session.commit()
    except Exception as e:
        print(f"Exception {e}")
        postgres_one_session.rollback()
        postgres_two_session.rollback()
    finally:
        print("Finally")
        postgres_one_session.close()
        postgres_two_session.close()


def create_users_context_manager_session():
    with with_session_logic() as (_postgres_one_session, _postgres_two_session,):
        users = [User(name=f"PG#1_user_{n}") for n in range(constants.CREATE_USERS)]
        accounts = [Account(name=f"PG#2_account_{n}") for n in range(constants.CREATE_ACCOUNTS)]

        _postgres_one_session.bulk_save_objects(users)
        _postgres_two_session.bulk_save_objects(accounts)

from contextlib import contextmanager

from postgres1_session import Postgres1DbSession
from postgres2_session import Postgres2DbSession
from models import User


@contextmanager
def multi_db_connection():
    postgres_1 = Postgres1DbSession()
    postgres_2 = Postgres2DbSession()

    postgres_1.begin()
    postgres_2.begin()

    try:
        postgres_1.prepare()
        postgres_2.prepare()
        print("Before yield")
        yield postgres_1, postgres_2
        print("Before commit")
        postgres_1.commit()
        # raise ValueError("OMG")
        postgres_2.commit()
    except Exception as e:
        print(f"Exception {e}")
        postgres_1.rollback()
        postgres_2.rollback()
    finally:
        print("Finally")
        postgres_1.close()
        postgres_2.close()


def create_users():
    with multi_db_connection() as (_postgres_1, _postgres_2):
        _postgres_1.add(
            User(name="Postgres1")
        )
        _postgres_2.add(
            User(name="Postgres1")
        )


def create_users_2():
    postgres_1_session = Postgres1DbSession()
    postgres_2_session = Postgres2DbSession()

    postgres_1_session.begin()
    postgres_2_session.begin()

    try:
        postgres_1_users = [User(name=f"PG#1_user_{n}") for n in range(10000)]
        postgres_2_users = [User(name=f"PG#2_user_{n}") for n in range(10000)]

        postgres_1_session.bulk_save_objects(postgres_1_users)
        postgres_2_session.bulk_save_objects(postgres_2_users)

        postgres_1_session.prepare()
        postgres_2_session.prepare()

        postgres_1_session.commit()
        raise ValueError("Some error!")
        # postgres_1_session should be rolled back
        postgres_2_session.commit()
    except BaseException as e:
        print(f"Exception: {e}. Rolling back sessions...")
        postgres_1_session.rollback()
        postgres_2_session.rollback()


create_users_2()
# create_users()

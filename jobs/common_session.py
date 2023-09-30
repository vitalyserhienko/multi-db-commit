from db.db_session import Session
from db.one.models import User
from db.two.models import Account


def create_users_combined_session():
    with Session() as session, session.begin():
        users = [User(name=f"PG#1_user_{n}") for n in range(10000)]
        accounts = [Account(name=f"PG#2_account_{n}") for n in range(10000)]

        session.bulk_save_objects(users)
        session.bulk_save_objects(accounts)

        session.prepare()
        session.commit()

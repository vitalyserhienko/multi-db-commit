from contextlib import contextmanager

# from postgres1_session import Postgres1DbSession
# from postgres2_session import Postgres2DbSession
# from models import User


# @contextmanager
# def multi_db_connection():
#     postgres_1 = Postgres1DbSession()
#     postgres_2 = Postgres2DbSession()
#
#     postgres_1.begin()
#     postgres_2.begin()
#
#     try:
#         postgres_1.prepare()
#         postgres_2.prepare()
#         print("Before yield")
#         yield postgres_1, postgres_2
#         print("Before commit")
#         postgres_1.commit()
#         # raise ValueError("OMG")
#         postgres_2.commit()
#     except Exception as e:
#         print(f"Exception {e}")
#         postgres_1.rollback()
#         postgres_2.rollback()
#     finally:
#         print("Finally")
#         postgres_1.close()
#         postgres_2.close()
#
#
# def create_users():
#     with multi_db_connection() as (_postgres_1, _postgres_2):
#         _postgres_1.add(
#             User(name="Postgres1")
#         )
#         _postgres_2.add(
#             User(name="Postgres1")
#         )

# def create_users_2():
#     postgres_1_session = Postgres1DbSession()
#     postgres_2_session = Postgres2DbSession()
#
#     postgres_1_session.begin()
#     postgres_2_session.begin()
#
#     try:
#         postgres_1_users = [User(name=f"PG#1_user_{n}") for n in range(10000)]
#         postgres_2_users = [User(name=f"PG#2_user_{n}") for n in range(10000)]
#
#         postgres_1_session.bulk_save_objects(postgres_1_users)
#         postgres_2_session.bulk_save_objects(postgres_2_users)
#
#         postgres_1_session.prepare()
#         postgres_2_session.prepare()
#
#         postgres_1_session.commit()
#         raise ValueError("Some error!")
#         # postgres_1_session should be rolled back
#         postgres_2_session.commit()
#     except BaseException as e:
#         print(f"Exception: {e}. Rolling back sessions...")
#         postgres_1_session.rollback()
#         postgres_2_session.rollback()

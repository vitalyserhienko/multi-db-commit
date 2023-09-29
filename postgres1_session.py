from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine_from_config


engine = engine_from_config(
    configuration={"db.url": "postgresql://postgres:postgres@localhost:5432/db"},
    prefix="db.",
    pool_pre_ping=True,
    hide_parameters=True,
    echo=True,
)

Postgres1DbSession = sessionmaker(bind=engine, twophase=True)

from sqlalchemy.orm import sessionmaker

from db.one.db_engine import engine as db_one_engine
from db.one.models import User
from db.two.db_engine import engine as db_two_engine
from db.two.models import Account

Session = sessionmaker(twophase=True)

# Enabling Two-Phase Commit
# https://docs.sqlalchemy.org/en/14/orm/session_transaction.html#enabling-two-phase-commit
Session.configure(binds={User: db_one_engine, Account: db_two_engine})
